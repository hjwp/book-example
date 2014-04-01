# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(serialize=False, primary_key=True, max_length=254)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
