# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 18:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_produkt_cena'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tosell',
            name='zamowienie',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='account.Zamowienie'),
        ),
    ]
