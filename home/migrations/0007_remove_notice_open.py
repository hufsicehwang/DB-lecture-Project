# Generated by Django 3.2.8 on 2021-12-10 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_email_notice_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='open',
        ),
    ]