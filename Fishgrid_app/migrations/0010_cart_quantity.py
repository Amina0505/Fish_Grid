# Generated by Django 4.0.3 on 2022-03-21 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fishgrid_app', '0009_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=0, null=True),
        ),
    ]