# Generated by Django 4.1.1 on 2022-12-21 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BurgerApi', '0011_alter_ordermaster_orderno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='addOns',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='quantity',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='ordermaster',
            name='orderNo',
            field=models.CharField(blank=True, default=941774828, max_length=100000000000),
        ),
    ]