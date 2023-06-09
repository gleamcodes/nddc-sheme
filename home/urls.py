from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home_view"),
    path('save_image/', views.save_image, name='save_image'),
    path("extract-user-data/", views.ExtractUserDataView.as_view(), name="extract_user_data")
]
