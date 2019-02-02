# Generated by Django 2.1.4 on 2019-02-02 07:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Threads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thread_name', models.CharField(max_length=200)),
                ('thread_creation_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('thread_creator_user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Users.Users')),
            ],
        ),
    ]
