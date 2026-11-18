from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError



class Specialty(models.Model):
    name = models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=true)
    updated_at=models.DateTimeField(auto_now=true)

class User(AbstractUser):
    pass

class Doctor(User):
    license_number = models.CharField(max_length=6, unique=True)
    phone = models.CharField(max_length=8)
    specialties = models.ManyToManyField(Specialty,related_name='doctors')
    created_at=models.DateTimeField(auto_now_add=true)
    updated_at=models.DateTimeField(auto_now=true)
    #specialty =models.ManyToManyField("AccountApp.Speciality")
    specialty =models.ManyToManyField(Specialty, related_name='doctors',)
    number_validator =RegexValidator(regex=r'^\d{8}$',message="le numero doit contenir exactement 8 chiffres.")
    def validate_birth_date(v):
        if v>=timezone.localdate():
            raise ValidationError("la date de naissance ne peut pas etre dans le future .")
class Patient(User):
    national_id = models.CharField(max_length=8, unique=True)
    phone = models.CharField(max_length=8)
    birth_date = models.DateField()
    created_at=models.DateTimeField(auto_now_add=true)