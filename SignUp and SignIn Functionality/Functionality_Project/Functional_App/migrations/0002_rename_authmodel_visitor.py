# Generated by Django 4.2.7 on 2024-08-09 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Functional_App', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AuthModel',
            new_name='Visitor',
        ),
    ]