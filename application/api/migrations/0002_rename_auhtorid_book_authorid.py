# Generated by Django 4.0.4 on 2022-05-26 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='auhtorID',
            new_name='authorID',
        ),
    ]
