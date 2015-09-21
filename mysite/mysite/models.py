from django.db import models
from django.contrib.auth.models import User
from mysite.ListField import ListField

class UserProfile(models.Model):
    # This line is required. It links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    street_address = models.CharField(max_length=60, blank=True)
    city = models.CharField(max_length=25, blank=True)
    state = models.CharField(max_length=25, default = "None", blank=True)
    zipcode = models.CharField(max_length = 5, blank=True)
    country = models.CharField(max_length=25, blank=True)
    about = models.CharField(max_length=1000, blank=True)

    country_requested = models.CharField(max_length=50, blank=True)
    countries_requested_list = ListField()

    rating = models.IntegerField(blank=True, null = True)

    website = models.URLField(blank = True)
    # picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class UserUpdate(models.Model):

    #user = models.OneToOneField(User)

    first_name = models.CharField(max_length = 40, blank=True)
    last_name = models.CharField(max_length = 40, blank=True)
    new_password = models.CharField(max_length = 60, blank=True)
    confirm_password = models.CharField(max_length = 60, blank=True)
    email = models.EmailField(max_length = 60, blank=True)

    def __unicode__(self):
        return self.user.username


class SelectCountry(models.Model):
    add_country = models.CharField(max_length=50, blank=True)
    
    

    def __unicode__(self):
        return self.user.username






