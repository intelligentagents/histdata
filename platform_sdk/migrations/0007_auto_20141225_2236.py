# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('platform_sdk', '0006_auto_20141225_1836'),
    ]

    operations = [
        migrations.RenameField(
            model_name='change',
            old_name='idCommit',
            new_name='commit_obj',
        ),
        migrations.RenameField(
            model_name='change',
            old_name='idEntity',
            new_name='entity_obj',
        ),
        migrations.AlterUniqueTogether(
            name='change',
            unique_together=set([('commit_obj', 'entity_obj', 'desc')]),
        ),
    ]
