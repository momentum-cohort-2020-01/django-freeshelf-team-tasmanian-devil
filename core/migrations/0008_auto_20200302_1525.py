# Generated by Django 3.0.3 on 2020-03-02 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='imagefile',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='imagefile',
            new_name='image',
        ),
    ]
