# Generated by Django 4.1.1 on 2022-10-03 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BurgerApi', '0013_alter_category_category_alter_order_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(blank=True, choices=[('Burger', 'Burger'), ('Pizza', 'Pizza'), ('Kacchi', 'Kacchi'), ('Biriyani', 'Biriyani')], default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='catergory',
            field=models.OneToOneField(blank=True, choices=[('Burger', 'Burger'), ('Pizza', 'Pizza'), ('Kacchi', 'Kacchi'), ('Biriyani', 'Biriyani')], default=None, on_delete=django.db.models.deletion.CASCADE, to='BurgerApi.category'),
            preserve_default=False,
        ),
    ]
