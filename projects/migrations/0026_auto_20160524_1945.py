# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0025_projectobjectcount_object_count_field_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectobjectcount',
            name='object_count_field_name',
            field=models.CharField(default='meta.count', max_length=40),
        ),
    ]
