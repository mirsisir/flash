# Generated by Django 3.0.8 on 2020-09-17 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0035_order_order_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-date_created']},
        ),
    ]
