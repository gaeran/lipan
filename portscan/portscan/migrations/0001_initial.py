# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-26 00:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScanResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=20)),
                ('service', models.CharField(max_length=70)),
            ],
        ),
    ]
