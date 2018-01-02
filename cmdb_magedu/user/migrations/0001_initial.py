# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-02 00:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('age', models.IntegerField()),
                ('telephone', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('register_time', models.DateTimeField(auto_now_add=True)),
                ('login_time', models.DateTimeField()),
            ],
        ),
    ]