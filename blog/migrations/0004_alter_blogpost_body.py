# Generated by Django 5.2.3 on 2025-06-26 03:06

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogpost_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
