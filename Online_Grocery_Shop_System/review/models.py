from django.db import models

# Create your models here.
class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    userid = models.IntegerField(db_column='Userid')  # Field name made lowercase.
    review = models.CharField(max_length=300)
    date = models.CharField(max_length=200)
    product_id = models.IntegerField()
    rating = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'review'