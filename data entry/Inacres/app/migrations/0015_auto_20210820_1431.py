# Generated by Django 3.2.6 on 2021-08-20 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20210820_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document_details',
            name='aadhar_photo',
            field=models.ImageField(help_text='Upload Aadhar Image..', upload_to='app/'),
        ),
        migrations.AlterField(
            model_name='document_details',
            name='passbook_photo',
            field=models.ImageField(help_text='Upload passbook Image..', upload_to='app/'),
        ),
    ]
