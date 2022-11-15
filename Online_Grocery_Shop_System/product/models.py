from django.db import models

# Create your models here.
class Product(models.Model):
    prod_id = models.AutoField(primary_key=True)
    productname = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    stock = models.CharField(max_length=200)
    shopid = models.IntegerField()
    image = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'product'
        