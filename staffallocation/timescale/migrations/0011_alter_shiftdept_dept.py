# Generated by Django 4.0.3 on 2022-04-24 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timescale', '0010_alter_shiftdept_dept_alter_shiftdept_shift'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shiftdept',
            name='dept',
            field=models.CharField(max_length=40),
        ),
    ]
