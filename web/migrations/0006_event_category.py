# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_event_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.CharField(max_length=30, choices=[(0, 'Koodikoulu'), (1, 'Koodikerho'), (2, 'Muu')], default=(0, 'Koodikoulu')),
        ),
    ]
