# Generated by Django 2.2.1 on 2019-05-26 19:55

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('test', models.CharField(max_length=255, null=True)),
                ('subheading', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='test_image')),
                ('body', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', tinymce.models.HTMLField(verbose_name='Content')),
                ('draft', models.BooleanField(default=False)),
                ('date', models.IntegerField(null=True)),
                ('year', models.IntegerField(null=True)),
                ('month', models.CharField(max_length=255, null=True)),
                ('image', models.ImageField(blank=True, upload_to='test_image')),
                ('test', models.IntegerField(null=True)),
            ],
        ),
    ]
