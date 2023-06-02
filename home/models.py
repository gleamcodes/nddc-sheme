from django.db import models

# Create your models here.

class ApplicantDetail(models.Model):
    appliacant_image = models.ImageField(blank=True, null=True, upload_to="applicant_photo")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    tradeType = models.CharField(max_length=255)
    accountNumber = models.CharField(max_length=255)
    bankName = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=255)
    lga = models.CharField(max_length=255)
    albumSerialNumber = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)