from rest_framework import serializers

from . import models


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'name']


class DiscountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Discount
        fields = ['id', 'percent', 'fix_price', 'start_time', 'deadline', 'total_price']


class DishSerializer(serializers.HyperlinkedModelSerializer):
    discount = DiscountSerializer()
    price = serializers.FloatField()

    class Meta:
        model = models.Dish
        fields = ['id', 'name', 'category', 'discount', 'category_id', 'photo', 'price', 'weight',
                  'ingredients', 'total_price']


class ClientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Client
        fields = ('name', 'phone')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    client = ClientSerializer()
    dishes = serializers.PrimaryKeyRelatedField(
        write_only=True,
        many=True, required=True, queryset=models.Dish.objects.all(),
    )

    class Meta:
        model = models.Order
        fields = ['id', 'dishes', 'client']

    def create(self, validated_data):
        dishes = validated_data.pop('dishes')
        client = models.Client.objects.create(**validated_data.pop('client'))
        order = models.Order.objects.create(**validated_data, client=client)

        models.Position.objects.bulk_create(
            [models.Position.make(order, dish) for dish in dishes],
        )
        return order
