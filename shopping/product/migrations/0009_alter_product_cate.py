# Generated by Django 4.1 on 2024-08-30 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_product_cate_cartitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cate',
            field=models.CharField(blank=True, choices=[('Electronics', 'Electronics'), ('Groccery', 'Groccery'), ('Fruit', 'Fruit'), ('Vegitables', 'Vegitbales')], max_length=20),
        ),
    ]
