# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20150903_1010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='time',
        ),
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2015, 9, 4, 9, 31, 26, 537898, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2015, 9, 4, 9, 31, 35, 639858, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
