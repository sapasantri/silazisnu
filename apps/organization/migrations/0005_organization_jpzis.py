# Generated by Django 2.2.16 on 2020-09-23 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20200923_0734'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='jpzis',
            field=models.IntegerField(default=0),
        ),
    ]
