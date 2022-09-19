# Generated by Django 4.1.1 on 2022-09-19 22:12

import dj_kaos_utils.models.fields
import dj_kaos_utils.models.mixins
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import rules.contrib.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_archived', models.BooleanField(default=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('price', dj_kaos_utils.models.fields.MoneyField()),
            ],
            options={
                'abstract': False,
            },
            bases=(dj_kaos_utils.models.mixins.HasAutoFields, rules.contrib.models.RulesModelMixin, models.Model),
        ),
    ]
