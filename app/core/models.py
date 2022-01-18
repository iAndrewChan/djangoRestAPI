from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

# Create your models here.


class UserManager(BaseUserManager):

    # https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#writing-a-manager-for-a-custom-user-model
    # https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#a-full-example
    # https://docs.djangoproject.com/en/4.0/topics/db/models/

    def create_user(self, password: str, **extra_fields):
        """creates and saves a new User"""

        self._validate_password("User", password)
        user = self.model(**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#django.contrib.auth.models.CustomUserManager.create_superuser
    def create_superuser(self, email: str, password: str):
        """creates and saves a new super user"""
        if not email:
            raise ValueError("Superuser must have an email")
        self._validate_password("Superuser", password)
        user = self.model(email=self.normalize_email(email))
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def _validate_password(self, user_type: str, password: str):
        # Validation
        # custom exception message
        if not password:
            raise ValueError(f"{user_type} must have a password set")
        if len(password) < 4:
            raise ValueError(f"{user_type} password must have at least 4 characters")


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using employee_id instead of username"""

    # https://docs.djangoproject.com/en/4.0/topics/auth/default/#user-objects
    # Only one class of user exists in Django’s authentication framework, i.e.,
    # 'superusers' or admin 'staff' users are just user objects
    # with special attributes set, not different classes of user objects.

    # https://docs.djangoproject.com/en/4.0/ref/contrib/auth/#fields
    # https://stackoverflow.com/questions/43472012/django-python-3-assertionerror-a-model-cant-have-more-than-one-autofield
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    # unique=True and blank=True set. In this situation, null=True is required to avoid
    # unique constraint violations when saving multiple objects with blank values.
    email = models.EmailField(unique=True, max_length=255, blank=True, null=True)

    # https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#authorization-for-inactive-users
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "employee_id"
