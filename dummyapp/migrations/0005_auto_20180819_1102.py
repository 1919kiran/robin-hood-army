# Generated by Django 2.0.2 on 2018-08-19 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummyapp', '0004_auto_20180819_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authmodel',
            name='image',
            field=models.FileField(default='settings.MEDIA_ROOT/abba.png', upload_to='media'),
        ),
    ]
