from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as text

from .manager import CustomUserManager
import uuid

class CustomUser(AbstractUser):

    username = None
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(text("email address"), blank=False, unique=True)
    first_name = models.CharField(text("first name"), max_length=150, blank=False)
    last_name = models.CharField(text("last name"), max_length=150, blank=False)
    date_of_birth = models.DateField(text("date of birth"), max_length=150, blank=False)
    verified = models.BooleanField(text("verified"), default=False)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email