# Generated by Django 3.1.4 on 2021-05-13 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviewapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='questionname',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
