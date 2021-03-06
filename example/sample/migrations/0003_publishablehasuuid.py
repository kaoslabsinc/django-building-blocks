# Generated by Django 3.2.5 on 2021-07-22 22:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0002_archivablehasuuid'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublishableHasUUID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('publishing_stage', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published'), ('archived', 'Archived')], default='draft', max_length=30)),
                ('publishing_stage_changed_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
