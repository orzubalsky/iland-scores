# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='score',
            options={'ordering': ['project', 'event', 'name']},
        ),
        migrations.RemoveField(
            model_name='score',
            name='date',
        ),
        migrations.AddField(
            model_name='score',
            name='year',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
