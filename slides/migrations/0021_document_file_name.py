# Generated by Django 3.1 on 2020-08-25 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0020_auto_20200825_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='file_name',
            field=models.CharField(default='something.jpg', max_length=256),
        ),
    ]
