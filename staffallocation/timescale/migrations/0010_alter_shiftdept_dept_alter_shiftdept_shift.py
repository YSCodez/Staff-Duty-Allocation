# Generated by Django 4.0.3 on 2022-04-24 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timescale', '0009_shiftdept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shiftdept',
            name='dept',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='shiftdept',
            name='shift',
            field=models.CharField(max_length=35),
        ),
    ]
