# Generated by Django 2.1.5 on 2020-01-02 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='date_updated',
        ),
    ]
