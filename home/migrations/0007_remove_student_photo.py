# Generated by Django 2.2.2 on 2019-07-04 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20190702_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='photo',
        ),
    ]
