# Generated by Django 3.2.7 on 2021-10-03 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_lists', '0007_auto_20211002_2228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='text',
        ),
        migrations.AlterField(
            model_name='project',
            name='details',
            field=models.TextField(),
        ),
    ]
