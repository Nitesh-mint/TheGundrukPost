from django.contrib.auth.models import AbstractUser # Importing the default user model to extend in the future if needed
from django.db import models

class User(AbstractUser):
    pass

