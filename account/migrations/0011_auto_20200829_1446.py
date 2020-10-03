# Generated by Django 3.0.8 on 2020-08-29 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20200829_0318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='receive',
        ),
        migrations.AddField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='condition',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Return', 'Return'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('new order', 'new order'), ('hold', 'hold')], default='new order', max_length=200, null=True),
        ),
    ]