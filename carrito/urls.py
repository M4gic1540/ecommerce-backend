from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarritoViewSet, ItemCarritoViewSet

router = DefaultRouter()
router.register(r'carritos', CarritoViewSet)
router.register(r'items', ItemCarritoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
