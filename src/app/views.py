from unicodedata import category
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
import re
import sweetify

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
  get_referencements = get_referencement({'publish':True})

  template_name = 'app/index.html'
  context = {
    'page':{
      'title': 'De-missa | Bienvenue',
      'text_title': 'De quels services avez-vous besoin ?',
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
     #------------------------------------------
    'get_referencements': get_referencements,

  }
  return render(request, template_name, context)


def service(request):
  get_something_service = get_services({'publish':True})
  get_infos_web = get_info_web({'publish':True})
  get_referencements = get_referencement({'publish':True})

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
     #-----------------------------------
    'get_referencements': get_referencements,
  }
  return render(request, template_name, context)


def under_service(request, service_slug):
  get_related_services =  get_related_service(service_slug)
  get_infos_web = get_info_web({'publish':True})
  get_socials =   get_social({'publish':True})

  template_name = 'app/under-service.html'
  context = {
    'page':{
      'title': 'De-missa | ' + service_slug,
      },
    'is_true': True,
    'get_socials': get_socials,
    'get_related_services': get_related_services,
    'get_infos_web': get_infos_web,
  }
  return render(request, template_name, context)


def under_service_under(request, service_slug):
  get_related_services =  get_related_service(service_slug)
  get_infos_web = get_info_web({'publish':True})
  get_referencements = get_referencement({'publish':True})
  get_socials =   get_social({'publish':True})

  template_name = 'app/detail-service.html'
  context = {
      'page':{
        'title': 'De-missa | ' + service_slug,
        'text_title': ' Tous nos service ' + service_slug,
      },
      'get_related_services' : get_related_services,
      'get_socials': get_socials,
      'get_infos_web': get_infos_web,
      'is_link': True,
      #---------------------------------------
      'get_referencements': get_referencements,
  }
  print("########1########")
  return render(request, template_name, context)


def reserve(request, sous_service_slug ):

  get_infos_sousService = get_info_sousService(sous_service_slug)
  get_banner = get_banners({'publish':True})
  get_infos_web = get_info_web({'publish':True})
  get_socials =   get_social({'publish':True})
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
    'get_socials': get_socials,
    'sous_service_slug': sous_service_slug,
    'get_infos_sousService': get_infos_sousService
  }
  return render(request, template_name, context)

@csrf_exempt
def postDataContact(request):

  all_is_true = False
  msg = ''

  name = request.POST.get('name')
  email = request.POST.get('email')
  phone = request.POST.get('phone')
  message = request.POST.get('message')

  if not name or name.isspace() or not email or email.isspace() or not phone or phone.isspace():
    msg = 'Veuillez renseigner les champs vides'
  elif len(phone) < 10:
    msg = 'Le numéro de téléphone doit etre e 10 chiffres'
  elif verify_email(email):
    msg = 'veuillez saisir un addresse Mail correct'
  else:
    all_is_true, msg = True, 'Vous receverez un email'
    print('############# 1 ###############')
    contact_customer, created = Contact.objects.get_or_create(name=name, email=email, phone=phone, message=message)
    print(created)
    if created:
      msg = "ce message est déjà envoyé"
    else:
      contact_customer.save()


  data = {
    'success': all_is_true,
    'msg': msg
  }
  return JsonResponse(data,safe=False)



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
    all_is_true, msg = True, 'Vous recevrez un email'

  phone = "+"+ str(225)+phones

  print(phone)
  reserved,created = Commandes.objects.get_or_create(name=name, phone=phone, service=service)


  if created:
   
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
    reserved.save()
    msg="Réservation effectuée"
    print("###############  4  #####################")

  else:
    print(f'bonjour M. {name} Vous avez demande un service de {service} le {date} à {time}' )
    print(f'bonjour M. {name} a demande un service de {service} le {date} à {time} Son numero est le {phone}')
    msg = "Votre réservation est déjà en cour de traitement"

  
  data = {
    'success': all_is_true,
    'msg': msg
  }
  return JsonResponse(data,safe=False)




def conditionGeneral(request):
  get_infos_web = get_info_web({'publish':True})
  get_condition_generals = get_condition_general({'publish':True})
  get_socials =   get_social({'publish':True})

  template_name = "app/condition.html"
  context={
    'page':{
      'title': 'De-missa | CGU',
    },
    'get_infos_web': get_infos_web,
    'get_socials': get_socials,
    'get_condition_generals': get_condition_generals,
  }
  return render(request, template_name, context)


def contact(request):
  get_infos_web = get_info_web({'publish':True})
  get_socials =   get_social({'publish':True})

  template_name = "app/contact.html"
  context={
    'page':{
      'title': 'De-missa | contact',
    },
    'get_infos_web': get_infos_web,
    'get_socials': get_socials,
  }
  return render(request, template_name, context)


def sitemaps_xml(request):

  template_name = 'app/sitemap.xml'
  context = {
    
  }
  return render(request, template_name, context)

def inscription(request):
  get_infos_web = get_info_web({'publish':True})
  get_banner = get_banners({'publish':True})
  get_all_under_services = get_all_under_service({'publish':True})
  get_metiers = get_metier({'publish': True})
  get_socials =   get_social({'publish':True})

  if request.method == 'POST':
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    address = request.POST.get('address')
    service = request.POST.get('service')
    confirm = request.POST.get('confirm')
    profile = request.FILES.get('profile')
    recto = request.FILES.get('recto')
    verso = request.FILES.get('verso')
  

    pattern = r'^(01|05|07)\d{8}$'
    chaine_de_caracteres = '0176543210'


    if confirm =="on":
      print(service)
      
      if not name or name.isspace() or not address or address.isspace() or not phone or phone.isspace():
        sweetify.error(request, 'Veuillez remplir tous les champs', button='Ok', timer=None)

      elif not len(phone):
        sweetify.error(request, 'Votre numéro doit etre de 10 chiffres', button='Ok', timer=None)

      elif profile is None:
        sweetify.error(request, 'Veuillez selectionner une photo de vous', button='Ok', timer=None)
      
      elif service == "1":
        sweetify.error(request, 'Veuillez choisir un service dans lequel vous souhaitez prester', button='Ok', timer=None)
        
      elif (recto and verso) is None:
        sweetify.error(request, 'Veuillez selectionner le recto et le verso de votre pièce d\'identité', button='Ok', timer=None)

      elif not re.match(pattern, phone):
        sweetify.error(request, 'Votre numéro doit etre de 10 chiffres et commencer par 01 ou 05 ou 07', button='Ok', timer=None)

      else :
        prestataire, created = Prestatire.objects.get_or_create(
          name=name, 
          email=email, 
          phone=phone, 
          address=address, 
          service=service, 
          profile=profile,
          recto=recto, 
          verso=verso
          )
        
        if created:
        
          subject = "Devenir jobber chez DE-MISSA"
          subjects = "DE-MISSA"
          message = f"Bonjour M./Mde/Mdle {name}  \nVous etes maintenant un jobber de DE-MISSA exerçant dans le service {service} \n\n\n\n MERCI POUR VOTRE CONFIANCE"
          messages = f'bonjour M {name} vient de s\'inscrire en temps que jobber dans le {service}\nSon numero est le {phone}'
          from_email = settings.EMAIL_HOST_USER
          customer_email = email
          print("###############  1  #####################")
          to_list = [email]
          to_lists = [settings.EMAIL_HOST_USER]
          print("###############  2  #####################")
          send_mail(subject, message, from_email, to_list, fail_silently=False)
          print("###############  3  #####################")
          send_mail(subjects, messages, customer_email, to_lists,fail_silently=False)
          prestataire.save()
          msg="Réservation effectuée"
          print("###############  4  #####################")
          sweetify.success(request, 'Prestataire crée', button='Ok', timer=None)
          return redirect("welcome")
        else:
          msg = "Votre réservation est déjà en cour de traitement"
          sweetify.success(request, 'Prestataire déjà créé', button='Ok', timer=None)
    else:
      sweetify.error(request, 'Veuillez cocher Nos conditions générales d\'utilisations', button='Ok', timer=None)

  template_name = "app/inscription.html"
  context={
    'page':{
      'title': 'De-missa | CGU',
    },
    'get_infos_web': get_infos_web,
    'get_banner': get_banner,
    'get_all_under_services': get_all_under_services,
    'get_socials': get_socials,
    'get_metiers': get_metiers
  }
  return render(request, template_name, context)


def mentionLegal(request):
  get_socials =   get_social({'publish':True})
  get_infos_web = get_info_web({'publish':True})
  get_mention_legals = get_mention_legal({'publish':True})

  template_name = "app/mention.html"
  context={
    'page':{
      'title': 'De-missa | CGU',
    },
    'get_infos_web': get_infos_web,
    'get_socials': get_socials,
    'get_mention_legals': get_mention_legals,
  }
  return render(request, template_name, context)
