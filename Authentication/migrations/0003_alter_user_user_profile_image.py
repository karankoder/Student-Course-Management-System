# Generated by Django 4.2.6 on 2023-11-07 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0002_user_department_user_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_profile_image',
            field=models.ImageField(upload_to='profile_pics'),
        ),
    ]