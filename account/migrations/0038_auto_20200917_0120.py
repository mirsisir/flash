# Generated by Django 3.0.8 on 2020-09-17 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0037_auto_20200917_0100'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-order_date1',)},
        ),
    ]
