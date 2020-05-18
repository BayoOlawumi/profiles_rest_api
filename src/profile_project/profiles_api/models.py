from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
#Access Level of Users
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    """Helps django work with our custom user model"""
    def create_user(self, email, name, password=None):
        """Create a new user profile object"""
        if not email:
            raise ValueError("Users must have an email address")
        email=self.normalize_email(email)
        user=self.model(email=email,name=name)

        user.set_password(password)
        #Save on the Database it is currently connected to
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        """Create and save a given superuser using given details"""
        user=self.create_user(email,name,password)
        user.is_superuser=True
        user.is_staff=True
       #Save on the Database it is currently connected to
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Represents User Profile inside our system"""
    email=models.EmailField(max_length=255, unique=True)
    name=models.CharField(max_length=255)
    Is_active= models.BooleanField(default=True)
    Is_staff=models.BooleanField(default=False)


    objects=UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=["name"]

    #Helper Functions
    def get_full_name(self):
        """Use to get a users fullname"""

        return self.name

    def get_short_name(self):
        """Use to get a users short name"""

        return self.name

    def __str__(self):
        """Django uses this one to convert the object to a string"""

        return self.email
