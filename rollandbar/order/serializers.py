from rest_framework import serializers

from . import models


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'name']


class DiscountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Discount
        fields = ['id', 'percent', 'fix_price', 'start_time', 'deadline', 'total_dish_price']


class DishSerializer(serializers.HyperlinkedModelSerializer):
    discount = DiscountSerializer()  # TODO добавить логику получения скидки

    class Meta:
        model = models.Dish
        fields = ['id', 'name', 'category', 'discount', 'category_id', 'photo', 'price', 'weight',
                  'ingredients']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Order
        fields = ['receiving_date']


"""
api/categories
api/dishes # фильр по категориям

"""
