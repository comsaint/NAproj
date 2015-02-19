# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0004_auto_20150216_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.AddField(
            model_name='question',
            name='vote_count_ABSTAIN',
            field=models.IntegerField(default=0, db_column='ABSTAIN'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='vote_count_NO',
            field=models.IntegerField(default=0, db_column='NO'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='vote_count_YES',
            field=models.IntegerField(default=0, db_column='YES'),
            preserve_default=True,
        ),
    ]
