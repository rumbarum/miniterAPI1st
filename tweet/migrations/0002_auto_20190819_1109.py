# Generated by Django 2.2.4 on 2019-08-19 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='content',
            new_name='user_content',
        ),
        migrations.RenameField(
            model_name='tweet',
            old_name='iddd',
            new_name='user_id',
        ),
    ]