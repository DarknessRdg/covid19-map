# Generated by Django 3.0.6 on 2020-05-17 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='File name to be ran function main()', max_length=255, unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
