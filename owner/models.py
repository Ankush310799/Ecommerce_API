
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import date



class User(AbstractUser):
        username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
        email = models.EmailField(max_length=50, unique = True,)
        shop_name = models.CharField(max_length=100,blank = True)
        address = models.CharField(max_length = 200,blank = True)
        phone_no = models.CharField(max_length = 10,blank = False,)
        is_owner = models.BooleanField(default=False)
        created_at = models.DateTimeField(auto_now_add=True)


        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

        def __str__(self):
          if self.shop_name:
            result = self.shop_name
          else:
            result = self.first_name +" "+ self.last_name
          return result
