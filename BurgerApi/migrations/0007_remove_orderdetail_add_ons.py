# Generated by Django 4.1.1 on 2023-02-01 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BurgerApi', '0006_customerdetail_city_customerdetail_house_no_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetail',
            name='add_ons',
        ),
    ]