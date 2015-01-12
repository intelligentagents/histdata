# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('platform_sdk', '0008_auto_20141226_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entity',
            name='code',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='entity',
            unique_together=set([('code', 'isPublic')]),
        ),
    ]
