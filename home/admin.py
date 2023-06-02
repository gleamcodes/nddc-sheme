from django.contrib import admin
from .models import ApplicantDetail

# Register your models here.

class ApplicantDetailAdmin(admin.ModelAdmin):
    #fields = ["post_title", "post_image", "post_content", "meta_description", "category"]
    list_display = ("first_name", "last_name", "tradeType", "lga", "timestamp")
    list_filter = ("timestamp", "lga", "bankName",)
    search_fields = ("first_name", "last_name", "accountNumber", "phoneNumber")
admin.site.register(ApplicantDetail, ApplicantDetailAdmin)
