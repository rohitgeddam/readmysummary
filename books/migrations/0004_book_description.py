# Generated by Django 3.1.1 on 2020-09-29 15:54

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20200929_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=ckeditor.fields.RichTextField(default=''),
        ),
    ]
