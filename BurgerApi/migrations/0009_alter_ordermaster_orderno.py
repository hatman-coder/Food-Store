# Generated by Django 4.1.1 on 2022-12-21 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BurgerApi', '0008_alter_ordermaster_orderno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermaster',
            name='orderNo',
            field=models.IntegerField(auto_created=True),
        ),
    ]