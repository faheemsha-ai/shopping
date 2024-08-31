# Generated by Django 4.1 on 2024-08-30 06:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0007_alter_product_cate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cate',
            field=models.CharField(blank=True, choices=[('Electronics', 'Electronics'), ('Fruit', 'Fruit'), ('Vegitables', 'Vegitbales'), ('Groccery', 'Groccery')], max_length=20),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
