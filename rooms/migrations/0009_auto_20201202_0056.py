# Generated by Django 2.2.5 on 2020-12-01 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0008_auto_20201202_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]
