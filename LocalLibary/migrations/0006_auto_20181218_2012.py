# Generated by Django 2.1.4 on 2018-12-18 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LocalLibary', '0005_auto_20181218_2008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='author_about',
            new_name='about',
        ),
    ]
