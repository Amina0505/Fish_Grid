# Generated by Django 4.0.3 on 2022-03-22 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fishgrid_app', '0012_compalaint'),
    ]

    operations = [
        migrations.AddField(
            model_name='compalaint',
            name='action',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='compalaint',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='compalaint',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='compalaint',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
    ]