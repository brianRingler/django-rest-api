from profiles_project.settings import AUTH_PASSWORD_VALIDATORS
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


'''One limitation of custom user models is that installing a custom user model
 will break any proxy model extending User 
 
 '''


class UserProfileManager(BaseUserManager):
    '''Manager for user profiles'''
    def create_user(self, email, name, password=None):
        '''Create a new user profile'''
        if not email:
            raise ValueError('Users must have an email address')

        
        email = self.normalize_email(email),
        user = self.model(email=email, name=name) 
        
        # use Django set_password function to convert to hashed password (encrypted) 
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, name, password=None):
        '''Create a new superuser profile'''
        user = self.create_user(email, name, password) # ORDER MATTERS - name, email need to match (self, name, email, password)

        # is_superuser is created automatically by PermissionsMixin
        user.is_superuser = True

        # is_staff was created in UserProfile class  
        user.is_staff = True
        user.save(using=self._db)

        return user




class UserProfile(AbstractBaseUser, PermissionsMixin):
    '''Database model for users in the system'''
    email = models.EmailField(max_length=225, unique=True, blank=False)
    name = models.CharField(max_length=255, blank=False )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    
    # Django out of box uses username for login credentials. We want to use an email 
    # We are overriding the default username with email required for login
    USERNAME_FIELD = 'email'
    # adding the required field will force user to add name when logging-in
    # by default Django will require the username which we converted to email and password
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        '''Retrieve the full name of user'''
        return self.name
    
    def get_short_name(self):
        '''Retrieve short name of user'''
        return self.name

    def __str__(self):
        '''Return string representation of our user'''
        return f'{self.id} {self.email} {self.name}' 