# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-14 23:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20170114_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='produkt',
            name='cena',
            field=models.FloatField(default=99999),
        ),
    ]
