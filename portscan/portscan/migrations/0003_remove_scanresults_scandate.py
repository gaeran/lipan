# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-26 21:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portscan', '0002_auto_20170425_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scanresults',
            name='scanDate',
        ),
    ]