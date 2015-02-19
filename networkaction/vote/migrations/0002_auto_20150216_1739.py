# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='question_title',
        ),
        migrations.AddField(
            model_name='question',
            name='question_description',
            field=models.TextField(default='No decription.', max_length=2000),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='vote_count_abstain',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='vote_count_no',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='vote_count_yes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
