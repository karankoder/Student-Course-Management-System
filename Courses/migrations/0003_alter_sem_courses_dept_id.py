# Generated by Django 4.2.6 on 2023-11-06 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0002_alter_announcement_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sem_courses',
            name='dept_id',
            field=models.CharField(choices=[('CSE', 'CSE'), ('MNC', 'MNC'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('MEC', 'MEC'), ('CER', 'CER'), ('CHE', 'CHE'), ('CIV', 'CIV'), ('MET', 'MET'), ('MIN', 'MIN'), ('PHE', 'PHE'), ('APD', 'APD')], max_length=50),
        ),
    ]