# Generated by Django 3.2.7 on 2021-10-02 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_lists', '0006_project_due_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='done',
            old_name='topic',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='progress',
            old_name='topic',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='topic',
            new_name='project',
        ),
    ]