# Generated by Django 2.0.3 on 2018-03-29 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keyword',
            name='workflow',
        ),
        migrations.AddField(
            model_name='workflow',
            name='keyword',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
        migrations.DeleteModel(
            name='KeyWord',
        ),
    ]