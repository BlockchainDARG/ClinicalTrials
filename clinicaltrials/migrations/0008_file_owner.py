# Generated by Django 2.0.1 on 2018-01-22 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clinicaltrials', '0007_remove_file_file_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
