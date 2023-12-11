from rest_framework.serializers import ModelSerializer
from .models import Manager, Product, Order
from datetime import datetime


class ManagerSerializer(ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data["timestamp"] = datetime.now()

        return data


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["timestamp"] = datetime.now()
        data["manager"] = ManagerSerializer(Manager.objects.filter(id=data["manager"]).first()).data

        return data


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
