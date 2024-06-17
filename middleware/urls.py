# myapp/urls.py

from django.urls import path
from .views import b2c_request_view

urlpatterns = [
    path('zamtel-request/', b2c_request_view, name='zamtel_request'),
]
