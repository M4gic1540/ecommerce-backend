from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Carrito, ItemCarrito
from .serializers import CarritoSerializer, ItemCarritoSerializer
from productos.models import Producto
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

Usuario = get_user_model()

class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

    def perform_create(self, serializer):
        usuario = self.request.user
        serializer.save(usuario=usuario)

    @action(detail=False, methods=['get'])
    def mi_carrito(self, request):
        usuario = request.user
        carrito, created = Carrito.objects.get_or_create(usuario=usuario)
        serializer = CarritoSerializer(carrito)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def agregar_item(self, request, pk=None):
        carrito = self.get_object()
        producto = get_object_or_404(Producto, id=request.data.get('producto'))
        cantidad = request.data.get('cantidad', 1)
        item, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
        if not created:
            item.cantidad += int(cantidad)
            item.save()
        serializer = ItemCarritoSerializer(item)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def eliminar_item(self, request, pk=None):
        carrito = self.get_object()
        producto = get_object_or_404(Producto, id=request.data.get('producto'))
        item = get_object_or_404(ItemCarrito, carrito=carrito, producto=producto)
        item.delete()
        return Response(status=204)

class ItemCarritoViewSet(viewsets.ModelViewSet):
    queryset = ItemCarrito.objects.all()
    serializer_class = ItemCarritoSerializer
