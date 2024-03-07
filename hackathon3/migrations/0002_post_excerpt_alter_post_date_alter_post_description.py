# Generated by Django 4.2.11 on 2024-03-07 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon3', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='excerpt',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]