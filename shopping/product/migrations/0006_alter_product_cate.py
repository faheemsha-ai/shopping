# Generated by Django 4.1 on 2024-08-29 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_cate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cate',
            field=models.CharField(blank=True, choices=[('Groccery', 'Groccery'), ('Fruit', 'Fruit'), ('Vegitables', 'Vegitbales')], max_length=20),
        ),
    ]
