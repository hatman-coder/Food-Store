# Generated by Django 4.1.1 on 2023-01-10 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BurgerApi', '0029_alter_orderstatus_order_placed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderstatus',
            name='order_placed',
            field=models.BooleanField(default=True, editable=False),
        ),
    ]
