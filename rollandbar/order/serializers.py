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


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Order
        fields = ['receiving_date']
