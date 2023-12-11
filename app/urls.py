from django.urls import path
from .views import (

    ManagerListAPIView, ManagerCreateAPIView, ManagerRUDView,
    ProductListAPIView, ProductCreateAPIView,
    ProductRUDView, OrderCreateAPIView, OrderRUDView, OrderListAPIView


)
urlpatterns = [
    path('', ProductListAPIView.as_view()),
    path('products/', ProductListAPIView.as_view()),
    path('product/', ProductCreateAPIView.as_view()),
    path('product/<int:pk>/', ProductRUDView.as_view()),

    path('managers/', ManagerListAPIView.as_view()),
    path('manager/', ManagerCreateAPIView.as_view()),
    path('manager/<int:pk>/', ManagerRUDView.as_view()),


    path('orders/', OrderListAPIView.as_view()),
    path('order/<int:pk>/', OrderRUDView.as_view()),
    path('order/', OrderCreateAPIView.as_view())

]
