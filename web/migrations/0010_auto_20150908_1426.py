# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20150904_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(max_length=30, default=('ENSIASKELEET', 'Koodikoulu ensiaskeleet'), choices=[('ENSIASKELEET', 'Koodikoulu ensiaskeleet'), ('ILTIS', 'Koodikoulu iltis'), ('OTHER', 'Muu')]),
        ),
    ]
