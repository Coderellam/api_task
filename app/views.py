from django.shortcuts import render

from .models import Manager, Order, Product

from rest_framework import generics
import requests
from .serializer import ManagerSerializer, OrderSerializer, ProductSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from django.conf import settings
from .permissions import IsSuperUser
from rest_framework.permissions import IsAuthenticated


class ManagerListAPIView(ListAPIView):
    serializer_class = ManagerSerializer
    queryset = Manager.objects.all()
    permission_classes = (IsSuperUser,)


class ManagerRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ManagerSerializer
    queryset = Manager.objects.all()
    permission_classes = (IsSuperUser,)


class ManagerCreateAPIView(generics.CreateAPIView):
    serializer_class = ManagerSerializer
    queryset = Manager.objects.all()
    permission_classes = (IsAuthenticated,)


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (IsSuperUser,)


class ProductRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (IsSuperUser,)


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class OrderListAPIView(ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = (IsSuperUser,)


class OrderRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsSuperUser,)


class OrderCreateAPIView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def post(self, request, *args, **kwargs):
        message_str = f"name: {request.data['name']}, phone: {request.data['contact']}," \
                      f" message: {request.data['quantity']} "
        # f"product name: {request.data['product_name']}, quantity: {request.data['quantity']}}"
        requests.get(settings.TELEGRAM_URL.format(message_str))
        return self.create(request, *args, **kwargs)

