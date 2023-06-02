from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from .models import ApplicantDetail
from django.core.files.base import ContentFile
import base64
from django.contrib import messages
import cloudinary.uploader


# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home/index.html")
    
    def post(self, request, *args, **kwargs):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        tradeType = request.POST.get("tradeType")
        accountNumber = request.POST.get("accountNumber")
        bankName = request.POST.get("bankName")
        lga = request.POST.get("lga")
        albumSerialNumber = request.POST.get("albumSerialNumber")
        phoneNumber = request.POST.get("phoneNumber")
        employmentStrength = request.POST.get("employmentStrength")
        print(first_name)
        print(last_name)
        print(tradeType)
        print(accountNumber)
        print(bankName)
        print(lga)
        print(phoneNumber)
        print(employmentStrength)
        context = {
            "first_name":first_name,
            "last_name":last_name,
            "tradeType":tradeType,
            "accountNumber":accountNumber,
            "bankName":bankName,
            "lga":lga,
            "albumSerialNumber":albumSerialNumber,
            "phoneNumber":phoneNumber,
            "employmentStrength":employmentStrength
        }
        return render(request, "home/capture-image.html", context)
        

def save_image(request):
    if request.method == 'POST':
        image_data = request.POST.get('image_data')
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        tradeType = request.POST.get("tradeType")
        accountNumber = request.POST.get("accountNumber")
        bankName = request.POST.get("bankName")
        lga = request.POST.get("lga")
        albumSerialNumber = request.POST.get("albumSerialNumber")
        phoneNumber = request.POST.get("phoneNumber")
        employmentStrength = request.POST.get("employmentStrength")

        # Convert Base64 data to image file
        format, imgstr = image_data.split(';base64,')
        ext = format.split('/')[-1]
        image_file = ContentFile(base64.b64decode(imgstr), name=f'image.{ext}')

        folder_name = 'applicant_photo'  # Specify the folder name here
        # Upload image to Cloudinary with folder specified
        upload_result = cloudinary.uploader.upload(image_file, folder=folder_name)
        image_url = upload_result['secure_url']

        # # Create a new Image instance and save it to the database
        new_applicant = ApplicantDetail(applicant_image=image_url, employmentStrength=employmentStrength, phoneNumber=phoneNumber, albumSerialNumber=albumSerialNumber, first_name=first_name, last_name=last_name, tradeType=tradeType, accountNumber=accountNumber, bankName=bankName, lga=lga)
        new_applicant.save()
        messages.success(request, 'Applicant Registered Successfully')
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
