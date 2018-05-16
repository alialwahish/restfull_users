# Generated by Django 2.0.5 on 2018-05-15 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='city',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dojo',
            name='state',
            field=models.CharField(default='', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dojo',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]