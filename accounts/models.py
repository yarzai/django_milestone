from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

# Create your models here.

TYPES = [
    ("editor", "Editor"),
    ("developer", "Developer"),
    ("designer", "Designer")
]


class AccountManager(BaseUserManager):
    def create_user(self, email, name, user_type, age=12, password=None):
        """ Create a new user profile """
        if not email:
            raise ValueError("User must have an Email")

        user = self.model(email=email, name=name)
        user.set_password(password)
        user.user_type = user_type
        user.age = age
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, user_type, password=None):
        """ Create and save superuser """

        if not email:
            raise ValueError("User must have email")

        user = self.model(email=email, name=name)

        user.set_password(password)
        user.user_type = user_type
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=250)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    user_type = models.CharField(max_length=150, choices=TYPES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_type', 'name']

    objects = AccountManager()

    class Meta:
        db_table = 'account'
        verbose_name = "account"
        verbose_name_plural = "accounts"

    def __str__(self):
        return self.name
