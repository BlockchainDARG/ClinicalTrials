# Generated by Django 2.0.1 on 2018-01-26 22:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clinicaltrials', '0015_auto_20180124_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(blank=True, null=True)),
                ('hashString', models.CharField(blank=True, max_length=500, null=True)),
                ('previousHash', models.CharField(blank=True, max_length=500, null=True)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('fileReference', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clinicaltrials.file')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
