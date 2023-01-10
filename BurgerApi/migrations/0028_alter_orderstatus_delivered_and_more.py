# Generated by Django 4.1.1 on 2023-01-10 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BurgerApi', '0027_alter_orderstatus_order_placed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderstatus',
            name='delivered',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='orderstatus',
            name='order_confirmed',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='orderstatus',
            name='order_placed',
            field=models.BooleanField(auto_created=True, default=True, editable=False),
        ),
        migrations.AlterField(
            model_name='orderstatus',
            name='order_preparation',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='orderstatus',
            name='out_for_delivery',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
