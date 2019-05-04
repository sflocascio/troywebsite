# Generated by Django 2.2 on 2019-05-04 15:54

from django.db import migrations, models


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
                ('subtitle', models.CharField(max_length=255)),
                ('subheading', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='test_image')),
                ('body', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'About',
            },
        ),
    ]
