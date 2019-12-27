# Generated by Django 3.0.1 on 2019-12-24 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='building',
        ),
        migrations.RemoveField(
            model_name='address',
            name='street',
        ),
        migrations.AddField(
            model_name='address',
            name='first_line',
            field=models.CharField(default='test', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='second_line',
            field=models.CharField(max_length=256, null=True),
        ),
    ]