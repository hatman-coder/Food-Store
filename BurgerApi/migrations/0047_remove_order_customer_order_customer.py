# Generated by Django 4.1.1 on 2022-10-11 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BurgerApi', '0046_alter_order_products_alter_product_addones_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ManyToManyField(blank=True, to='BurgerApi.customerdetail'),
        ),
    ]
