# Generated by Django 4.1.7 on 2023-05-21 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beta', '0002_remove_audio_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='names',
            field=models.CharField(default=False, max_length=500, null=True),
        ),
    ]
