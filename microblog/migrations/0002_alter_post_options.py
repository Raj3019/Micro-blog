# Generated by Django 5.0.2 on 2024-02-21 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('microblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('post', 'author')},
        ),
    ]
