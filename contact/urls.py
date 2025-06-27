# contact/urls.py
from django.urls import path
from .views import ContactMessageView

urlpatterns = [
    path("submit/", ContactMessageView.as_view(), name="contact-submit"),
]
