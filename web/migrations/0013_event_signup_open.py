# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='signup_open',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
