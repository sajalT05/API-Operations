# Generated by Django 4.0.4 on 2022-05-26 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_auhtorid_book_authorid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='categoryId',
            new_name='categoryID',
        ),
    ]