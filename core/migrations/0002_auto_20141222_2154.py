# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commit',
            name='id',
        ),
        migrations.RemoveField(
            model_name='entity',
            name='id',
        ),
        migrations.AlterField(
            model_name='commit',
            name='snapshot',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entity',
            name='code',
            field=models.CharField(max_length=255, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
