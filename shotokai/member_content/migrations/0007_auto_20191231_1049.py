# Generated by Django 3.0.1 on 2019-12-31 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member_content', '0006_auto_20191231_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='picture',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
