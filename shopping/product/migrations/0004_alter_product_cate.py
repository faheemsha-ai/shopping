# Generated by Django 4.1 on 2024-08-29 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_cate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cate',
            field=models.CharField(blank=True, choices=[('Fruit', 'Fruit'), ('Vegitables', 'Vegitbales'), ('Groccery', 'Groccery')], max_length=20),
        ),
    ]
