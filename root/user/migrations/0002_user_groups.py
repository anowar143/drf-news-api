# Generated by Django 2.2.13 on 2020-07-15 09:48

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='groups',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), default=list, size=None),
        ),
    ]
