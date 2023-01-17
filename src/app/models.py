from django.db import models


from autoslug import AutoSlugField
from twilio.rest import Client

# Create your models here.


class Convention(models.Model):
    publish = models.BooleanField(default=True)
    date_add = models.DateField(auto_now=False, auto_now_add=True)
    date_update = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True

class Web(Convention):
    name = models.CharField(max_length=50)
    picture = models.FileField(upload_to='img_web')
    description = models.TextField()
    
    class Meta:
        verbose_name = "Info du site"
        verbose_name_plural = "Infos du site"
    def __str__(self):
        return self.name


class Banner(Convention):
    title = models.CharField(max_length=250)
    picture = models.FileField(upload_to='img_banner')
    picturePhone = models.FileField(upload_to='img_banner')
    
    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"

    def __str__(self):
        return self.title
    

class Text(Convention):
    libele = models.TextField()
    description = models.TextField()
    
    class Meta:
        verbose_name = "Text"
        verbose_name_plural = "Texts"

    def __str__(self):
        return self.libele
    


class Quality(Convention):
    title = models.CharField(max_length=50)
    description = models.TextField()
    picture = models.FileField(upload_to='img_quality')

    class Meta:
        verbose_name = "Quality"
        verbose_name_plural = "Qualities"
    
    def __str__(self):
        return self.title

class AskService(Convention):
    title = models.CharField(max_length=50)
    description = models.TextField()
    order = models.IntegerField()
    picture = models.FileField(upload_to='img_ask_service')

    class Meta:
        verbose_name = "Procedure"
        verbose_name_plural = "Procedures"
    
    def __str__(self):
        return self.title
    

class About(Convention):
    title = models.CharField(max_length=50)
    description = models.TextField()
    picture = models.FileField(upload_to='img_about')

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "Abouts"

    def __str__(self):
        return self.title


class Social(Convention):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    link = models.URLField(max_length=200)
    
    class Meta:
        verbose_name = "Reseaux social"
        verbose_name_plural = "Reseaux sociaux"
    
    def __str__(self):
        return self.name
    


class Service(Convention):
    name = models.CharField(max_length=50)
    picture = models.FileField(upload_to="img_service")
    picture1 = models.FileField(upload_to="img_service")
    description = models.TextField()
    order = models.IntegerField()
    service_slug =  AutoSlugField(populate_from='name')
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.name


class SousService(Convention):
    name = models.CharField(max_length=50)
    picture = models.FileField(upload_to="img_service")
    libele = models.TextField()
    description = models.TextField()
    order = models.IntegerField()
    price = models.CharField(max_length=100)
    sous_service_slug =  AutoSlugField(populate_from='name')
    service = models.ForeignKey("Service", related_name="category_service", on_delete=models.SET_NULL, null=True)
    
    class Meta:
        verbose_name = "Sous Service"
        verbose_name_plural = "Sous Services"

    def __str__(self):
        return self.name


class Commandes(Convention):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=50)
    service = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        account_sid = 'ACa35b83c179182b2764a0ca2150aaa293' 
        auth_token = 'b8bc7a92f6a874b106030a5497612910' 
        client = Client(account_sid, auth_token) 
        
        message = client.messages.create(
            body=f'bonjour M {self.name} Vous avez demande un service de {self.service} \n\nMerci de vouloir patienter afin qu\'un agent vous appelle ',
            from_='+13608033691',
            to='+2250789773420'
        )
        return super().save(*args,**kwargs)