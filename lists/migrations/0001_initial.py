# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            options = {},
            name = 'List',
            bases = (models.Model,),
            fields = [('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),)],
        ),
        migrations.CreateModel(
            options = {},
            name = 'Item',
            bases = (models.Model,),
            fields = [('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),), ('text', models.TextField(),), ('list', models.ForeignKey(to_field='id', to='lists.List'),)],
        ),
    ]
