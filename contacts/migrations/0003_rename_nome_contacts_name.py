# Generated by Django 4.2 on 2023-04-27 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_alter_contacts_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacts',
            old_name='nome',
            new_name='name',
        ),
    ]
