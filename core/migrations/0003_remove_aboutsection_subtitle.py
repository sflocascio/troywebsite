# Generated by Django 2.2.1 on 2019-05-04 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190504_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutsection',
            name='subtitle',
        ),
    ]