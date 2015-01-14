# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20141222_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='change',
            name='desc',
            field=models.CharField(default=b'a', max_length=1, choices=[(b'a', b'ADDED'), (b'b', b'BODY_MODIFIED'), (b'c', b'CHANGED_RETURN_TYPE'), (b'd', b'DELETED'), (b'i', b'INCREASED_VISIBILITY'), (b'p', b'PARAMETER_ADDED'), (b'q', b'PARAMETER_REMOVED'), (b'u', b'REMOVED_THROWN_EXCEPTION'), (b'r', b'RENAMED'), (b'v', b'REDUCED_VISIBILITY'), (b't', b'THROWS_NEW_EXCEPTIONS'), (b'n', b'NONE')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entity',
            name='typeOfEntity',
            field=models.CharField(default=b'm', max_length=1, choices=[(b'm', b'METHOD'), (b'c', b'CLASS'), (b'p', b'SOURCE_PATH'), (b'n', b'n')]),
            preserve_default=True,
        ),
    ]
