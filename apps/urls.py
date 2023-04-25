from . import views
from django.urls import path

urlpatterns = [
    path("", views.index),
    path("output/", views.extract_resume_data)
]
