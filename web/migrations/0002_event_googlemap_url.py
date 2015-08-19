# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='googlemap_url',
            field=models.CharField(null=True, blank=True, max_length=255),
        ),
    ]
