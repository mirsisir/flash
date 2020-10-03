# Generated by Django 3.0.8 on 2020-09-14 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0030_extendeduser_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='pickup_address',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='shop_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
