# Generated by Django 3.2.23 on 2023-12-03 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20231203_1716'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_dat',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='updated_dat',
            new_name='updated_date',
        ),
    ]
