# Generated by Django 4.2.1 on 2023-06-02 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_applicantdetail_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicantdetail',
            name='employmentStrength',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
