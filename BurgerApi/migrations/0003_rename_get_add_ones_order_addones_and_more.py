# Generated by Django 4.1.1 on 2022-10-15 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BurgerApi', '0002_rename_getaddones_order_get_add_ones'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='get_add_ones',
            new_name='addOnes',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='addOnes',
            new_name='addOns',
        ),
    ]
