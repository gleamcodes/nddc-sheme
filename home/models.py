from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class ApplicantDetail(models.Model):
    applicant_image = CloudinaryField('image', blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    tradeType = models.CharField(max_length=255)
    accountNumber = models.CharField(max_length=255)
    bankName = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=255)
    lga = models.CharField(max_length=255)
    albumSerialNumber = models.IntegerField(blank=True, null=True)
    employmentStrength = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Applicant Details")
        verbose_name_plural = ("Applicant Details")
        ordering = ("albumSerialNumber",)

    def __str__(self):
        return f"{self.first_name} {self.last_name} details"