# Generated by Django 3.0.8 on 2020-08-30 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_auto_20200830_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='phone',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]