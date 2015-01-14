# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_entity_classname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='typeOfEntity',
            field=models.CharField(default=b'm', max_length=1, choices=[(b'm', b'METHOD'), (b'c', b'CLASS'), (b'p', b'SOURCE_FILE'), (b'n', b'NONE')]),
            preserve_default=True,
        ),
    ]
