from django.urls import path
from app.views import *

urlpatterns = [
    path('', home, name="welcome"),
    path('service', service, name="service"),
    path('<str:service_slug>/', under_service, name="sous-service"),
    path('service/<str:service_slug>/', under_service_under, name="service-middle-page"),
    path('confirmation', payment, name='payment'),
    path('postData', postData, name='postData')
]
