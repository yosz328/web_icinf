# Generated by Django 2.2.2 on 2019-06-26 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support_material', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='ffile',
            field=models.FileField(upload_to='', verbose_name='Archivo'),
        ),
    ]
