# Generated by Django 3.0.7 on 2020-09-19 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlshort', '0002_auto_20200919_1352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urls',
            old_name='shortquery',
            new_name='short_query',
        ),
    ]