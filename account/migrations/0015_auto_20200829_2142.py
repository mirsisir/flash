# Generated by Django 3.0.8 on 2020-08-29 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20200829_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_charge',
            field=models.IntegerField(null=True),
        ),
    ]
