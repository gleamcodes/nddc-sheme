# Generated by Django 4.2.1 on 2023-06-02 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_applicantdetail_appliacant_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicantdetail',
            name='phoneNumber',
            field=models.CharField(default='1', max_length=255),
        ),
    ]
