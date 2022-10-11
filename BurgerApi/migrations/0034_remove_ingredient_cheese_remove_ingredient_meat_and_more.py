# Generated by Django 4.1.1 on 2022-10-10 06:46

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('BurgerApi', '0033_alter_order_products_alter_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='cheese',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='meat',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='salad',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='ingredient',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('salad', 'Salad')], default=None, max_length=500),
            preserve_default=False,
        ),
    ]