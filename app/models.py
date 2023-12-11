from django.db import models
from django.contrib.auth.models import User

"""
menga API yozishiz kerak:
qaysi get qaysi post bo'ladi uni o'ziz aniqlashiz kerak.
men kak client sizga zakaz berayapman.
menda profile bo'lishi kerak(huddi adminga o'xshagan yoki author ga o'xshagan). 
profileda oddiy fullname age degan narsalar bo'ladi.
va men product qo'shaolishim kerak. keyin meni produktlarimni boshqalar sotib olaolishi 
uchun order degan API ham qilishiz kerak

"""


class Manager(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    fullname = models.CharField(max_length=40)
    age = models.IntegerField()
    is_stuff = models.BooleanField(default=False)

    def __str__(self):
        return self.fullname


class Product(models.Model):
    product_name = models.CharField(max_length=30)
    price = models.FloatField()
    picture = models.FileField(blank=True, null=True)

    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.product_name


class Order(models.Model):
    name = models.CharField(max_length=20)
    contact = models.IntegerField()
    address = models.CharField(max_length=30)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_solved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
