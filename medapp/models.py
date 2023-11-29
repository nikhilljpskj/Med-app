# med_app/models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
class MedStock(models.Model):
    med_name = models.CharField(max_length=255)
    usage = models.CharField(max_length=255)
    qty = models.IntegerField()

    def __str__(self):
        return self.med_name

class MedicalStore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=20, unique=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
