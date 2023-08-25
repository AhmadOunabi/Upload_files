# Generated by Django 4.2.4 on 2023-08-25 11:46

from django.db import migrations, models
import upload.validators


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.FileField(upload_to='files', validators=[upload.validators.valid_file]),
        ),
    ]
