from django.urls import path
from . import views

urlpatterns = [
    path('submit_request/', views.submit_request, name='submit_request'),
    path('request_tracking/', views.request_tracking, name='request_tracking'),
]