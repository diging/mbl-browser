# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-03 21:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0018_historicalposition_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalposition',
            name='changed_by',
        ),
        migrations.RemoveField(
            model_name='historicalposition',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalposition',
            name='person',
        ),
        migrations.RemoveField(
            model_name='historicalposition',
            name='validated_by',
        ),
        migrations.RemoveField(
            model_name='position',
            name='changed_by',
        ),
        migrations.RemoveField(
            model_name='position',
            name='person',
        ),
        migrations.RemoveField(
            model_name='position',
            name='validated_by',
        ),
        migrations.DeleteModel(
            name='HistoricalPosition',
        ),
        migrations.DeleteModel(
            name='Position',
        ),
    ]