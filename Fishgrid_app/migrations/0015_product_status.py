# Generated by Django 3.0.5 on 2022-03-23 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fishgrid_app', '0014_product_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
