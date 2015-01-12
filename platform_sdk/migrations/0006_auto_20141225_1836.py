# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('platform_sdk', '0005_auto_20141225_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='typeOfEntity',
            field=models.CharField(default=b'm', max_length=1, choices=[(b'm', b'METHOD'), (b'c', b'CLASS'), (b'p', b'SOURCE_PATH'), (b'n', b'NONE')]),
            preserve_default=True,
        ),
    ]
