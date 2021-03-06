# Generated by Django 3.0.1 on 2019-12-31 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member_content', '0011_auto_20191231_1313'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_line', models.CharField(max_length=256)),
                ('second_line', models.CharField(blank=True, max_length=256, null=True)),
                ('city', models.CharField(max_length=128)),
                ('state', models.CharField(max_length=2)),
                ('zip', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='member_content.HomeAddress'),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
