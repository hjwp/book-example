# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [('lists', '0001_initial')]

    operations = [
        migrations.AlterUniqueTogether(
            unique_together = set(['text', 'list']),
            name = 'item',
        ),
    ]
