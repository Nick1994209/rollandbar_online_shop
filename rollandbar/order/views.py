from rest_framework import mixins, viewsets

from . import models, serializers


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class DishViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Dish.objects.all()
    serializer_class = serializers.DishSerializer


class OrderViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


# '''
# Нужно добавить view
#
# POST /api/v1/orders/
#
#     {
#         user: {phone, address, name}
#         receiving_date: время привоза заказ
#         is_delivery: Доставка или самовывоз
#         positions: [
#             {
#                 dish_id,
#                 discount_id,
#             },
#         ]
#     }
#
#
#     # formdata
#     {
#         "user": {
#             "phone": "+791923219",
#             "address": "sadasdsa",
#             "name": "asddsa",
#         },
#         "receiving_date": "asdda".iso(),
#         "is_delivery": True,
#         "positions": [
#             123,
#             1254,
#             125322,
#         ],
#     }
# '''
