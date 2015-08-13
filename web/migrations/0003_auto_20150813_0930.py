# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20150807_0809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='first_name',
            new_name='child',
        ),
        migrations.RenameField(
            model_name='signup',
            old_name='last_name',
            new_name='guardian',
        ),
        migrations.AddField(
            model_name='signup',
            name='age',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='other',
            field=models.TextField(null=True, blank=True),
        ),
    ]
