# Generated by Django 4.1.1 on 2023-02-01 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BurgerApi', '0003_alter_ordermaster_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='product_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
