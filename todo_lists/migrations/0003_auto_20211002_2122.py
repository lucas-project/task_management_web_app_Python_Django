# Generated by Django 3.2.7 on 2021-10-02 11:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_lists', '0002_auto_20210920_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='Done',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateTimeField(default=datetime.datetime.now)),
                ('due_date', models.DateTimeField(default=datetime.datetime.now)),
                ('project_code', models.CharField(max_length=20)),
                ('details', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateTimeField(default=datetime.datetime.now)),
                ('due_date', models.DateTimeField(default=datetime.datetime.now)),
                ('project_code', models.CharField(max_length=20)),
                ('details', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=30)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('project_code', models.CharField(max_length=20)),
                ('details', models.CharField(max_length=200)),
                ('team', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateTimeField(default=datetime.datetime.now)),
                ('due_date', models.DateTimeField(default=datetime.datetime.now)),
                ('project_code', models.CharField(max_length=20)),
                ('details', models.CharField(max_length=200)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_lists.project')),
            ],
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.AddField(
            model_name='progress',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_lists.todo'),
        ),
        migrations.AddField(
            model_name='progress',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_lists.project'),
        ),
        migrations.AddField(
            model_name='done',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='todo_lists.todo'),
        ),
        migrations.AddField(
            model_name='done',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_lists.project'),
        ),
    ]
