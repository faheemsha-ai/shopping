# Generated by Django 4.1 on 2024-08-29 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_cate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cate',
            field=models.CharField(blank=True, choices=[('Vegitables', 'Vegitbales'), ('Groccery', 'Groccery'), ('Fruit', 'Fruit')], max_length=20),
        ),
    ]
