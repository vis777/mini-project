from django.db import models
from product.models import Product
# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    amount = models.IntegerField()
    quantity = models.FloatField()
    status = models.CharField(max_length=90)
    # prod_id = models.IntegerField()
    prod=models.ForeignKey(Product,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'order'

        
class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    price = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cart'