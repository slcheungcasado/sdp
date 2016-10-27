# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-27 00:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=8)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('staff_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='staff.Staff')),
            ],
            bases=('staff.staff',),
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('staff_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='staff.Staff')),
            ],
            bases=('staff.staff',),
        ),
    ]