# Generated by Django 2.0.1 on 2018-01-22 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicaltrials', '0009_auto_20180122_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
