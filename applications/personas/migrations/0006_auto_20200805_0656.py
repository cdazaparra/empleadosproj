# Generated by Django 3.1 on 2020-08-05 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0005_empleado_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre Completo'),
        ),
    ]
