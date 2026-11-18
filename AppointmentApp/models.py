from django.db import models
from django.conf import settings
from AccccountApp.models import Doctor,Patient

class Appointment(models.Model):
   reason =models.TextField()
   prescription =models.FileField(
        blank=true,
        upload_to='prescriptions/'
   )
class Status(models.TextChoices):
        PENDING = 'PENDING', 'En attente'
        CONFIRMED = 'CONFIRMED', 'Confirmé'
        CANCELLED = 'CANCELLED', 'Annulé'
status=models.CharField(max_length==10,choices==Status.choices,default=status.PENDING)

   

duration_minutes = models.PositiveIntegerField(default=30)
appointment_date = models.DateTimeField()
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
appointment_data = models.DateTimeField();
doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='appointments')
patient =models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='appointments')
