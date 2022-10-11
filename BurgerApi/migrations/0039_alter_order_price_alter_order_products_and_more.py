# Generated by Django 4.1.1 on 2022-10-10 08:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BurgerApi', '0038_rename_ingredient_addones_addones_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='BurgerApi.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]