# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_auto_20150908_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(max_length=30, default=('ENSIASKELEET', 'Koodikoulun ensiaskeleet'), choices=[('ENSIASKELEET', 'Koodikoulun ensiaskeleet'), ('ILTIS', 'Koodikoulun iltis'), ('OTHER', 'Muu')]),
        ),
    ]
