# Generated by Django 4.2.1 on 2023-06-02 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('tradeType', models.CharField(max_length=255)),
                ('accountNumber', models.CharField(max_length=255)),
                ('bankName', models.CharField(max_length=255)),
                ('lga', models.CharField(max_length=255)),
                ('albumSerialNumber', models.CharField(blank=True, max_length=255, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
