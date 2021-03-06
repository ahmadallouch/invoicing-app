# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 22:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('invoicing', '0002_auto_20170226_2012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_name', models.CharField(max_length=200)),
                ('address_line_1', models.CharField(max_length=100)),
                ('address_line_2', models.CharField(max_length=100)),
                ('bank_account', models.CharField(max_length=20, unique=True)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('VAT_number', models.CharField(max_length=20, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
