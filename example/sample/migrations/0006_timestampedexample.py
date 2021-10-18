# Generated by Django 3.2.5 on 2021-07-30 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0005_hasautofieldsexample'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeStampedExample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
