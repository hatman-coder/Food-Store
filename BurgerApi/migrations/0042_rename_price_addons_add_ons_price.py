# Generated by Django 4.1.1 on 2023-01-22 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BurgerApi', '0041_remove_addons_product_addons_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addons',
            old_name='price',
            new_name='add_ons_price',
        ),
    ]