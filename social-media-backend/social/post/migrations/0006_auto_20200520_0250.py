# Generated by Django 3.0.6 on 2020-05-20 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0006_auto_20200515_2340'),
        ('post', '0005_post_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_profile.UserProfile'),
        ),
    ]