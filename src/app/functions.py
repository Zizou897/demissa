import os
from django.shortcuts import get_object_or_404

from app.models import *


# Pour la page d'accueil (home) ------------------------------------------------

def get_info_web(data=dict()):
    return Web.objects.filter(**data).first()


def get_banners(data=dict()):
    return Banner.objects.filter(**data).first()


def get_texts(data=dict()):
    return Text.objects.filter(**data).first()


def get_qualities(data=dict()):
    return Quality.objects.filter(**data)


def get_ask_service(data=dict()):
    return AskService.objects.filter(**data).order_by('order')


def get_abouts(data=dict()):
    return About.objects.filter(**data).first()


def get_social(data=dict()):
    return Social.objects.filter(**data)


def get_something_services(data=dict()):
    return Service.objects.filter(**data).order_by('order')[:6]


def get_under_service(data=dict()):
    return SousService.objects.filter(**data).order_by('order')[:10]


#----------------------------------------------------------------------------------


# Pour la page des services (service) ------------------------------------------------

def get_services(data=dict()):
    return Service.objects.filter(**data).order_by('order')

#------------------------------------------------------------------------------------

# Pour la page des sous-services  en relation(service) ------------------------------------------------

def get_sous_service(data=dict()):
    return SousService.objects.get(**data)

def get_related_service(service_slug):
    return get_object_or_404(Service, service_slug=service_slug)


#------------------------------------------------------------------------------------

