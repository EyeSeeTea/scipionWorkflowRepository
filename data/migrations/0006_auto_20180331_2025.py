# Generated by Django 2.0.3 on 2018-03-31 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_auto_20180330_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workflow',
            name='description',
            field=models.TextField(blank=True, max_length=512, null=True),
        ),
    ]