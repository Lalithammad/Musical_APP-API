# Generated by Django 3.0.8 on 2021-01-12 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicmodel',
            name='song',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
