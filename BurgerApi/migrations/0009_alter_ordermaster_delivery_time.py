# Generated by Django 4.1.1 on 2023-01-10 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BurgerApi', '0008_alter_ordermaster_delivery_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermaster',
            name='delivery_time',
            field=models.CharField(default='10:55', editable=False, max_length=100),
        ),
    ]
