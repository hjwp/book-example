# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_item_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
