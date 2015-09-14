# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_auto_20150908_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='decoded_location',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
    ]
