# Generated by Django 3.1.4 on 2021-07-13 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviewapp', '0006_usertohandle'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='contest',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='index',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
