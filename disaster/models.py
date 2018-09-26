from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from .managers import UserManager
from django.conf import settings

state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'),blank=False,null=False)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    phone = models.CharField(_('phone'),max_length=30,unique=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'),default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    last_name  = models.CharField(_('last name'),max_length=30,blank=True)
    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

class state(models.Model):
    name = models.CharField(choices=state_choices,max_length=100)
class district(models.Model):
    state = models.ForeignKey(state, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

volunteer_category = (
    ('dcr', 'Doctor'),
    ('hsv', 'Health Services'),
    ('elw', 'Electrical Works'),
    ('mew', 'Mechanical Work'),
    ('cvw', 'Civil Work'),
    ('plw', 'Plumbing work'),
    ('vls', 'Vehicle Support'),
    ('ckg', 'Cooking'),
    ('rlo', 'Relief operation'),
    ('cln', 'Cleaning'),
    ('bot', 'Boat Service'),
    ('rck', 'Rock Climbing'),
    ('oth', 'Other')
)

gender =(
    (0,'Male'),
    (1,'Female'),
    (2,'Others')
)

class Volunteer(models.Model):
        name = models.CharField(max_length=100, verbose_name="Name")
        gender = models.IntegerField(choices = gender,verbose_name='Gender',null=True,blank=True)
        phone = models.CharField(max_length=14, verbose_name="Phone‍")
        district = models.CharField(max_length = 15,verbose_name="District")
        address = models.TextField(verbose_name="Address")
        area = models.CharField(max_length = 15,choices = volunteer_category,verbose_name = "Area of volunteering")

        joined = models.DateTimeField(auto_now_add=True)


        def __str__(self):
            return self.name


    
class Help(models.Model):
    name = models.CharField(max_length=200,blank=False,null=False)
    photo = models.ImageField(upload_to='help_photos/',blank=False,null=False)
    date = models.DateField(auto_now_add=True)

class Disasters(models.Model):
    name = models.CharField(max_length=30,blank=False,null=False)
    State = models.ForeignKey(state, on_delete=models.SET_NULL, null=True)
    District = models.ForeignKey(district, on_delete=models.SET_NULL, null=True)

 






