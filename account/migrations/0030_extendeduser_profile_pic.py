# Generated by Django 3.0.8 on 2020-09-14 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0029_auto_20200909_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendeduser',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
