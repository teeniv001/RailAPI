# Generated by Django 2.1.3 on 2019-02-06 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_pnrdetails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pnrdetails',
            old_name='pnr',
            new_name='pnrno',
        ),
    ]
