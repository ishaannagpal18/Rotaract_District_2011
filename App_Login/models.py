from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, User
# Create your models here.

class Individual(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rotaractor_or_interactor_or_rotarian = models.CharField(max_length=100, blank=False)
    auth_token = models.CharField(max_length=100, blank=False)
    name = models.CharField(max_length=100, blank=False)
    contact_no = models.CharField(max_length=100, blank=False)
    email_id = models.EmailField(max_length=30, blank=False)
    club_name = models.CharField(max_length=100, blank=False)
    club_rotary_id = models.CharField(max_length=30, blank=False)
    gender = models.CharField(max_length=100, blank=False)
    blood_group = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=100, blank=False)
    emergency_contact_name = models.CharField(max_length=100, blank=False)
    emergency_contact_no = models.CharField(max_length=100, blank=False)
    jacket_size = models.CharField(max_length=100, blank=False)
    participate_in_ryla = models.CharField(max_length=100, blank=False)
    theme_interest = models.CharField(max_length=100, blank=False)
    house_alloted = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + "'s Profile"



class Club(models.Model):
    rotaractor_or_interactor_or_rotarian = models.CharField(max_length=100, blank=True)
    auth_token = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    contact_no = models.CharField(max_length=100, blank=True)
    email_id = models.EmailField(max_length=30, blank=True)
    rotary_club_name = models.CharField(max_length=100, blank=True)
    interactor_club_name = models.CharField(max_length=100, blank=True)
    rotaractor_club_name = models.CharField(max_length=100, blank=True)
    club_rotary_id = models.CharField(max_length=30, blank=True)
    rotary_id = models.CharField(max_length=30, blank=True)
    club_email_id = models.EmailField(max_length=30, blank=True)
    parent_club_name = models.CharField(max_length=100, blank=True)
    presidents_name = models.CharField(max_length=100, blank=True)
    presidents_contact_no = models.CharField(max_length=100, blank=True)
    secretary_name = models.CharField(max_length=100, blank=True)
    secretary_contact_no = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    blood_group = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    emergency_contact_name = models.CharField(max_length=100, blank=True)
    emergency_contact_no = models.CharField(max_length=100, blank=True)
    jacket_size = models.CharField(max_length=100, blank=True)
    no_of_participants = models.CharField(max_length=100, blank=True)
    payment_screenshot = models.ImageField(upload_to="Payment_Screenshot" ,blank=True )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + "'s Profile"