# Generated by Django 3.1.3 on 2020-12-14 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memexplus', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basicbookmark',
            old_name='text',
            new_name='full_text',
        ),
        migrations.AddField(
            model_name='basicbookmark',
            name='stripped_text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
