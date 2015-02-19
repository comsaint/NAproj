# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0003_auto_20150216_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='vote_count_ABSTAIN',
            field=models.IntegerField(db_column='ABSTAIN', default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='choice',
            name='vote_count_NO',
            field=models.IntegerField(db_column='NO', default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='choice',
            name='vote_count_YES',
            field=models.IntegerField(db_column='YES', default=0),
            preserve_default=True,
        ),
    ]
