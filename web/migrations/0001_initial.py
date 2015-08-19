# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True, blank=True)),
                ('time', models.CharField(max_length=10)),
                ('price', models.PositiveIntegerField(default=0)),
                ('bring_along', models.CharField(null=True, blank=True, max_length=255)),
                ('street_address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=40)),
                ('requirements', models.TextField()),
                ('description', models.TextField()),
                ('organization', models.CharField(null=True, blank=True, max_length=100)),
                ('amount', models.PositiveIntegerField(null=True, blank=True)),
                ('signup_link', models.CharField(null=True, blank=True, max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('booked', models.BooleanField(default=False)),
                ('organizer', models.ForeignKey(related_name='events', blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('start_date',),
            },
        ),
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('child', models.CharField(max_length=100)),
                ('guardian', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(null=True, blank=True, max_length=100)),
                ('other', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(to='web.Event', related_name='participants')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
