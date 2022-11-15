from django.db import models

# Create your models here.
class Payment(models.Model):
    pay_id = models.AutoField(primary_key=True)
    card_holdername = models.CharField(max_length=20)
    cvv = models.CharField(max_length=20)
    card_number = models.CharField(max_length=20)
    amount = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'payment'