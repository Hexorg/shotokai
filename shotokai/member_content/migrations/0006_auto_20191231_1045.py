# Generated by Django 3.0.1 on 2019-12-31 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member_content', '0005_member_associated_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='picture',
            field=models.FilePathField(blank=True, null=True),
        ),
    ]
