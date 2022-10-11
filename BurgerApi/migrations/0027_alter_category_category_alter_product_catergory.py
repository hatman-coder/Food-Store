# Generated by Django 4.1.1 on 2022-10-10 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BurgerApi', '0026_alter_category_category_alter_product_catergory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('1', 'burger'), ('2', 'pizza')], max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='catergory',
            field=models.ForeignKey(blank=True, choices=[('1', 'burger'), ('2', 'pizza')], on_delete=django.db.models.deletion.CASCADE, to='BurgerApi.category'),
        ),
    ]