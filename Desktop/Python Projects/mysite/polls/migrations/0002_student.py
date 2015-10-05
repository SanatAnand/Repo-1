# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roll_no', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(regex=b'^.{9}$', message=b'Length has to be 9', code=b'nomatch')])),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
