# Generated by Django 4.1.1 on 2022-12-21 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BurgerApi', '0019_alter_ordermaster_orderno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermaster',
            name='orderNo',
            field=models.CharField(blank=True, default=4810354535, max_length=100000000000),
        ),
    ]