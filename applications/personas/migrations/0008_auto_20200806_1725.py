# Generated by Django 3.1 on 2020-08-06 22:25

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0007_auto_20200806_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='hoja_vida',
            field=ckeditor.fields.RichTextField(blank=True, max_length=200, null=True),
        ),
    ]
