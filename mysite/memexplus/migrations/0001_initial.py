# Generated by Django 3.1.3 on 2020-12-12 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='BasicBookmark',
            fields=[
                ('bookmark_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='memexplus.bookmark')),
                ('text', models.TextField()),
            ],
            bases=('memexplus.bookmark',),
        ),
    ]
