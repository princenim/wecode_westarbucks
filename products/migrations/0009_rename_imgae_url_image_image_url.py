# Generated by Django 3.2.4 on 2021-06-18 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_image_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='imgae_url',
            new_name='image_url',
        ),
    ]
