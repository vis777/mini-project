from django.db import models

# Create your models here.
class Registeration(models.Model):
    reg_id = models.AutoField(primary_key=True)
    first_name = models.CharField(db_column='First Name', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_name = models.CharField(db_column='Last Name', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters. 
    username = models.CharField(db_column='Username', max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50)  # Field name made lowercase.
    gender = models.CharField(max_length=50)
    email_id = models.CharField(max_length=50)
    place = models.CharField(db_column='Place', max_length=50)  # Field name made lowercase.
    post = models.CharField(max_length=50)
    pin = models.IntegerField()
    phone = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'registeration'