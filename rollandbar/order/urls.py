from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from . import views


router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'dishes', views.DishViewSet)
router.register(r'orders', views.OrderViewSet)

urlpatterns = [
    path('', TemplateView.as_view(template_name='core/index.html'), name='index'),
    path('api/v1/', include(router.urls)),

    path(
        'swagger-ui/',
        TemplateView.as_view(
            template_name='core/swagger-ui.html',
            extra_context={'schema_url': 'openapi-schema'},
        ),
        name='swagger-ui',
    ),
    path(
        'openapi',
        get_schema_view(
            title='Rollandbar',
            version='1.0.0',
            patterns=router.urls,
            url='/api/v1/',
        ),
        name='openapi-schema',
    ),
]
