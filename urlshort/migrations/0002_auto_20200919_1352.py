# Generated by Django 3.0.7 on 2020-09-19 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlshort', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urls',
            old_name='short_query',
            new_name='shortquery',
        ),
    ]
