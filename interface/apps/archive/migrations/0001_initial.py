# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('description', models.TextField()),
                ('place', models.CharField(max_length=100, null=True, blank=True)),
                ('city', models.CharField(max_length=100, null=True, blank=True)),
                ('state', models.CharField(max_length=2, null=True, blank=True)),
                ('country', models.CharField(max_length=100, null=True, blank=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('collaborators', models.TextField(null=True, blank=True)),
                ('event', models.ForeignKey(blank=True, to='archive.Event', null=True)),
                ('project', models.ForeignKey(blank=True, to='archive.Project', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
