# Generated by Django 3.1.7 on 2021-03-27 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('twitter_handle', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField()),
                ('text', models.TextField()),
            ],
        ),
    ]
