# Generated by Django 3.2.7 on 2021-10-05 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_lists', '0010_auto_20211003_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='resources',
            field=models.FileField(default=1, upload_to='uploads/%d/%m/%Y/'),
            preserve_default=False,
        ),
    ]
