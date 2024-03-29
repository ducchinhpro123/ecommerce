# Generated by Django 5.0.3 on 2024-03-16 13:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='product.product')),
                ('author', models.CharField(max_length=255)),
                ('pages', models.IntegerField()),
                ('publisher', models.CharField(max_length=255)),
                ('published_at', models.DateField()),
            ],
            bases=('product.product',),
        ),
    ]
