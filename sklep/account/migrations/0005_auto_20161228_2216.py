# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 21:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20161227_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.CharField(max_length=255, verbose_name='adres'),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=50, verbose_name='miasto'),
        ),
        migrations.AlterField(
            model_name='address',
            name='zipcode',
            field=models.CharField(max_length=150, verbose_name='kod pocztowy'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(max_length=17, unique=True),
        ),
        migrations.AlterField(
            model_name='usercd',
            name='fName',
            field=models.CharField(max_length=50, verbose_name='Imi\u0119'),
        ),
        migrations.AlterField(
            model_name='usercd',
            name='lName',
            field=models.CharField(max_length=50, verbose_name='nazwisko'),
        ),
        migrations.AlterField(
            model_name='usercd',
            name='phone',
            field=models.CharField(max_length=12, verbose_name='nr.telefonu'),
        ),
    ]
