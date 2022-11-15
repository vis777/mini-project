from django.db import models

# Create your models here.
class Complaint(models.Model):
    com_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    complaint = models.CharField(max_length=200)
    date = models.CharField(max_length=20)
    reply = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'complaint'