# Generated by Django 2.2.2 on 2019-07-02 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_library_library_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='stu',
            new_name='book',
        ),
    ]
