# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('platform_sdk', '0007_auto_20141225_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commit',
            name='snapshot',
            field=models.CharField(max_length=100, unique=True, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entity',
            name='code',
            field=models.CharField(max_length=255, unique=True, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
