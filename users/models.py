from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from PIL import Image

#from service.models import Hospital

class User(AbstractUser):
    is_patient = models.BooleanField('patient status', default=False)
    is_doctor = models.BooleanField('doctor status', default=False)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
    date_registered = models.DateTimeField(default=timezone.now)
    health_problem = models.TextField(max_length = 200, default = 'nothing')
    height = models.FloatField(null = True)
    weight = models.FloatField(null = True)

    def __str__(self):
        return self.user.username

    def get_bmi(self):
        return round ( (self.weight/(self.height**2)), 3 )


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length = 200, null = True)
    education = models.CharField(max_length = 200, null = True)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
    #hospital = models.ForeignKey(Hospital,null=True, blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
