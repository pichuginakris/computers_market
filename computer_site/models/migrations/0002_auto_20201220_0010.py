# Generated by Django 2.2 on 2020-12-19 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maincategory',
            old_name='nameMainCategory',
            new_name='name_main_category',
        ),
    ]
