from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfileinfo(models.Model):
    
    my_user=models.OneToOneField(User,on_delete=models.CASCADE)

    #aditional
    portfolio_site=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.my_user.username
        
