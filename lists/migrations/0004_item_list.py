# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.ForeignKey(to_field='id', to='lists.List', default=None),
            preserve_default=True,
        ),
    ]
