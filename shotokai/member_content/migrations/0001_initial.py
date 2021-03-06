# Generated by Django 3.0.1 on 2019-12-24 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belt', models.CharField(choices=[('RED4', 'Red: 4Th Kyu'), ('ORNG', 'Orange: 3Rd Kyu'), ('GRN2', 'Green: 2nd Kyu'), ('BRWN', 'Brown: 1st Kyu'), ('BLK1', 'Black: 1st Dan'), ('BLK2', 'Black: 2nd Dan'), ('BLK3', 'Black: 3rd Dan'), ('BLK4', 'Black: 4th Dan'), ('BLK5', 'Black: 5th Dan')], default='RED4', max_length=4)),
                ('paid_until', models.DateField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
