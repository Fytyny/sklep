# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-14 01:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20170114_0202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produkt',
            name='cena',
        ),
    ]