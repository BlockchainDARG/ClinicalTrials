# Generated by Django 2.0.1 on 2018-02-28 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinicaltrials', '0018_file_version'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='version',
        ),
    ]
