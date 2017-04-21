# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 18:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatment_type', models.PositiveSmallIntegerField(choices=[(1, 'Manicure'), (2, 'Pedicure'), (3, 'Corte de cabello'), (4, 'Tinte'), (5, 'Masaje')])),
                ('start_datetime', models.DateTimeField(verbose_name='Start datime')),
                ('end_datetime', models.DateTimeField(blank=True, verbose_name='End datime')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dates_by_customer', to='userprofiles.UserProfile')),
                ('specialist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dates_by_specialist', to='userprofiles.UserProfile')),
            ],
            options={
                'verbose_name': 'Date',
                'verbose_name_plural': 'Dates',
            },
        ),
    ]
