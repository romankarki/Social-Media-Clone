# Generated by Django 3.0.6 on 2020-05-12 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bio', models.CharField(max_length=250)),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
