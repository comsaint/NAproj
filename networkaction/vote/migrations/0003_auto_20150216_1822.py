# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_auto_20150216_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(to='vote.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='question',
            name='vote_count_abstain',
        ),
        migrations.RemoveField(
            model_name='question',
            name='vote_count_no',
        ),
        migrations.RemoveField(
            model_name='question',
            name='vote_count_yes',
        ),
        migrations.AlterField(
            model_name='question',
            name='question_description',
            field=models.TextField(max_length=5000, default='No decription.'),
            preserve_default=True,
        ),
    ]
