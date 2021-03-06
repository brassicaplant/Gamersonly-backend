# Generated by Django 2.1.5 on 2019-02-06 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AllPlatforms', '0001_initial'),
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platforms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_platform_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='AllPlatforms.AllPlatforms')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Users.Users')),
            ],
        ),
    ]
