# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_event_googlemap_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='googlemap_url',
            new_name='lat',
        ),
        migrations.AddField(
            model_name='event',
            name='lng',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
