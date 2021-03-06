# Generated by Django 2.2.16 on 2020-09-18 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, help_text='Unselect this instead of deleting accounts.', verbose_name='active')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('pc', models.IntegerField(default=0)),
                ('mwc', models.IntegerField(default=0)),
                ('ranting', models.IntegerField(default=0)),
                ('level', models.IntegerField(default=0)),
                ('nama', models.TextField()),
            ],
            options={
                'verbose_name': 'organization',
            },
        ),
    ]
