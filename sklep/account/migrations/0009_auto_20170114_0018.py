# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-13 23:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_koszyk_zamowienie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pracownik',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='zamowienie',
            name='status',
            field=models.IntegerField(default=1, verbose_name='Obecny status'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zamowienie',
            name='statustime',
            field=models.DateTimeField(default=None, verbose_name='Czas zmiany'),
            preserve_default=False,
        ),
    ]
