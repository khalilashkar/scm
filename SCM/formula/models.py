import datetime
from django.db import models
from .validators import validate_file_extensison
from django import forms
from  django_countries.fields import CountryField
from django.utils.translation import ugettext_lazy as _
class Registration(models.Model):
    """
    Modèle de l'inscription
    """
    gender_CHOICES = (
        ('female', 'Female'),
        ('male', 'Male'),
        ('prefer not to say', 'prefer not to say'),

    )
    app_CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No'),

    )
    
    #Information of the person who apply 
    Application_number= models.AutoField(primary_key=True,default=None)
    gender = models.CharField( _("Gender"),max_length=30, choices=gender_CHOICES,null=True )
    first_name = models.CharField(_("first name"), max_length=30 )
    nick_name = models.CharField(max_length=255,null=True,blank=True, verbose_name="Nickname")
    last_name = models.CharField(max_length=255, null=True, verbose_name=" last_name")
    #birth information 
    birth_date = models.DateField(verbose_name="birth_date ")
    birth_place = models.CharField(max_length=255, verbose_name="birth_place")
    country = CountryField(max_length=255, verbose_name="Country")
    city = models.CharField(max_length=255,null=True, verbose_name="city")
    #Connection information 
    mail = models.EmailField(max_length=255, verbose_name="Mail")
    phone = models.CharField(max_length=255, blank=True, null=True,verbose_name="Phone ") 
    #education and jobs 
    educatton_level=models.CharField(max_length=255, blank=True, null=True, verbose_name="Education_Level ")  
    job= models.CharField(max_length=255, blank=True, null=True,verbose_name="Job ") 
    #start_date = models.DateField(verbose_name="date of start job  ",null=True,default='')
    adress1=models.CharField(max_length=255,blank=True,null=True,verbose_name="recnetly adress")
    country_rec=CountryField(max_length=255,verbose_name='Country_rec',default='some_value')
    # city_recent = models.CharField(max_length=255, verbose_name="city")

       
    comments = models.TextField(blank=True, null=True, verbose_name="Comments")
    #document_1 = models.FileField(upload_to='documents/',null=True,validators=[validate_file_extensison],verbose_name="Document_1")
    #document_2 = models.FileField(upload_to='documents/',null=True,validators=[validate_file_extensison],verbose_name="Document_2")
