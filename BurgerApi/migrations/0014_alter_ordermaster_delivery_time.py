# Generated by Django 4.1.1 on 2023-01-10 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BurgerApi', '0013_alter_ordermaster_delivery_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermaster',
            name='delivery_time',
            field=models.CharField(default='11:24:43', max_length=100),
        ),
    ]