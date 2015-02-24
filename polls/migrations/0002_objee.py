# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('objective_statement', models.CharField(max_length=500)),
                ('question', models.ForeignKey(to='polls.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
