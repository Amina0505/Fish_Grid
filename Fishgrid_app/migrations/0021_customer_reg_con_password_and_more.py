# Generated by Django 4.0.3 on 2022-04-19 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fishgrid_app', '0020_cart_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_reg',
            name='con_password',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='shopregistration',
            name='con_password',
            field=models.CharField(max_length=50, null=True),
        ),
    ]