from unicodedata import category
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail

from demissa import settings
from app.functions import *
from app.models import *
# Create your views here.


def verify_email(email):
    try:
        validate_email(email)
        return False
    except ValidationError:
        return True


def home(request):
  get_infos_web = get_info_web({'publish':True})
  get_banner = get_banners({'publish':True})
  get_text = get_texts({'publish':True})
  get_quality = get_qualities({'publish':True})
  get_ask_services = get_ask_service({'publish':True})
  get_about = get_abouts({'publish':True})
  get_socials =   get_social({'publish':True})
  get_something_service = get_something_services({'publish':True})
  get_under_services = get_under_service({'publish':True})

  template_name = 'app/index.html'
  context = {
    'page':{
      'title': 'De-missa | Bienvenue',
      'text_title': 'De quel service avez-vous besoins ?',
      'text_description': 'Pour chaque situation, trouvez le prestataire dont les compétences répondent à vos attentes et à votre niveau d’exigence.',
    },
    'get_infos_web': get_infos_web,
    'get_banner': get_banner,
    'get_text': get_text,
    'get_quality': get_quality,
    'get_ask_services': get_ask_services,
    'get_about': get_about,
    'get_socials': get_socials,
    'get_something_service': get_something_service,
    'get_under_services': get_under_services,
  }
  return render(request, template_name, context)


def service(request):
  get_something_service = get_services({'publish':True})
  get_infos_web = get_info_web({'publish':True}) 
  
  template_name = 'app/service.html'
  context = {
      'page':{
        'title': 'De-missa | Service',
        'text_title': ' Tous nos services ?',
        'text_description': '',
      },
    'is_true': True,
    'get_something_service': get_something_service,
      'get_infos_web': get_infos_web,
  }
  return render(request, template_name, context)


def under_service(request, service_slug):
  get_related_services =  get_related_service(service_slug)
  get_infos_web = get_info_web({'publish':True}) 

  template_name = 'app/under-service.html'
  context = {
    'page':{
      'title': 'De-missa | ' + service_slug,
      },
    'is_true': True,
    'get_related_services': get_related_services,
      'get_infos_web': get_infos_web,
  }
  return render(request, template_name, context)


def under_service_under(request, service_slug):
  get_related_services =  get_related_service(service_slug)
  get_infos_web = get_info_web({'publish':True})  
  
  template_name = 'app/detail-service.html'
  context = {
      'page':{
        'title': 'De-missa | ' + service_slug,
        'text_title': ' Tous nos service ' + service_slug,
      },
      'get_related_services' : get_related_services,
      'get_infos_web': get_infos_web,
      'is_link': True,
  }
  print("########1########")
  return render(request, template_name, context)


def reserve(request, sous_service_slug ):
  
  get_infos_sousService = get_info_sousService(sous_service_slug)
  get_banner = get_banners({'publish':True})
  get_infos_web = get_info_web({'publish':True})
  #sous = SousService.objects.filter('publish' == True)
  #get_sous_services = sous
  #print
  template_name = 'app/reservation.html'
  context = {
    'page':{
      'title': 'De-missa | Réservation',
    },
    'get_banner': get_banner,
    'get_infos_web': get_infos_web,
    'sous_service_slug': sous_service_slug,
    'get_infos_sousService': get_infos_sousService
  }
  return render(request, template_name, context)




@csrf_exempt
def postData(request):


  all_is_true = False
  msg = ''
  
  address = request.POST.get('address')
  time = request.POST.get('time')
  date = request.POST.get('date')
  nbr_pro = request.POST.get('nbr_pro')
  name = request.POST.get('name')
  email = request.POST.get('email')
  phones = request.POST.get('phone')
  message = request.POST.get('message')
  money = request.POST.get('money')
  service = request.POST.get('service')

          
  if not name or name.isspace() or not email or email.isspace() or not phones or phones.isspace():
    msg = 'Veuillez renseigner les champs vides'
  elif verify_email(email):
    msg = 'veuillez saisir un addresse Mail correct'
  elif len(phones) < 10:
    msg = 'Le numéro de téléphone doit etre e 10 chiffres'
  else:
    all_is_true, msg = True, 'Vous receverez un email '
  
  phone = "+"+str(225)+phones
  
  print(phone)
  reserved,created = Commandes.objects.get_or_create(name=name, phone=phone, service=service)
  if created:
    print(f'bonjour M. {name} Vous avez demande un service de manege le {date} à {time}' )
    print(f'bonjour M. {name} a demande un service de manege le {date} à {time} Son numero est le {phone}')
    reserved.save()
    
    
    subject = "Demande de service chez DE-MISSA"
    subjects = "DE-MISSA"
    message = f"Bonjour M./Mde/Mdle {name}  \nVous avez demande un service de manege pour {date} à {time}\n pour vos services à domicile \n\n\n\n MERCI POUR VOTRE CONFIANCE"
    messages = f'bonjour M {name} a demande un service de manege le {date} à {time} \nSon numero est le {phone}'
    from_email = settings.EMAIL_HOST_USER
    customer_email = email
    print("###############  1  #####################")
    to_list = [email]
    to_lists = [settings.EMAIL_HOST_USER]
    print("###############  2  #####################")         
    send_mail(subject, message, from_email, to_list, fail_silently=False)
    print("###############  3  #####################")
    send_mail(subjects, messages, customer_email, to_lists,fail_silently=False)
    print("###############  4  #####################")
  
  data = {
    'success': all_is_true,
    'msg': msg
  }
  return JsonResponse(data,safe=False)




def conditionGeneral(request):
  
  get_infos_web = get_info_web({'publish':True})
  
  template_name = "app/condition.html"
  context={
    'page':{
      'title': 'De-missa | CGU',
    },
    'get_infos_web': get_infos_web,
  }
  return render(request, template_name, context)


def contact(request):
  
  get_infos_web = get_info_web({'publish':True})
  
  template_name = "app/contact.html"
  context={
    'page':{
      'title': 'De-missa | contact',
    },
    'get_infos_web': get_infos_web,
  }
  return render(request, template_name, context)
  