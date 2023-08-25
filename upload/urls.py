from django.contrib import admin
from django.urls import path , include
from .views import file_upload

urlpatterns = [
    path('', file_upload)
]


