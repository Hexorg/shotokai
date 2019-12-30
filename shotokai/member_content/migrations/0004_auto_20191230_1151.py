# Generated by Django 3.0.1 on 2019-12-30 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member_content', '0003_auto_20191224_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='belt',
            field=models.CharField(choices=[('WHT5', 'White: 5Th Kyu'), ('RED4', 'Red: 4Th Kyu'), ('ORNG', 'Orange: 3Rd Kyu'), ('GRN2', 'Green: 2nd Kyu'), ('BRWN', 'Brown: 1st Kyu'), ('BLK1', 'Black: 1st Dan'), ('BLK2', 'Black: 2nd Dan'), ('BLK3', 'Black: 3rd Dan'), ('BLK4', 'Black: 4th Dan'), ('BLK5', 'Black: 5th Dan')], default='RED4', max_length=4),
        ),
    ]
