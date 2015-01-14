# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20150105_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='className',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
