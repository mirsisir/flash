# Generated by Django 3.0.8 on 2020-08-29 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20200829_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_charge',
            field=models.IntegerField(blank=True, default=60),
        ),
    ]
