# Generated by Django 3.1.1 on 2020-09-10 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
