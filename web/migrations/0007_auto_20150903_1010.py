# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_event_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(default=('SCHOOL', 'Koodikoulu'), max_length=30, choices=[('SCHOOL', 'Koodikoulu'), ('CLUB', 'Koodikerho'), ('OTHER', 'Muu')]),
        ),
    ]
