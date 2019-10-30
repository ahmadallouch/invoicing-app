# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-10-17 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0019_creditnote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditnote',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
