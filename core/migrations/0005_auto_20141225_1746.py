# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20141225_1738'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='change',
            unique_together=set([('idCommit', 'idEntity', 'desc')]),
        ),
    ]
