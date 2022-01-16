from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

# Create your models here.


class UserManager(BaseUserManager):
    # https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#a-full-example
    # https://docs.djangoproject.com/en/4.0/topics/db/models/

    def create_user(self, employee_id, password, **extra_fields):
        """creates and saves a new User"""
        user = self.model(employee_id=employee_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using employee_id instead of username"""

    # https://docs.djangoproject.com/en/4.0/ref/contrib/auth/#fields
    # https://stackoverflow.com/questions/43472012/django-python-3-assertionerror-a-model-cant-have-more-than-one-autofield
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    # https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#authorization-for-inactive-users
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "employee_id"
