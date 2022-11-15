# Generated by Django 3.2.15 on 2022-11-05 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('login_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'login',
                'managed': False,
            },
        ),
    ]