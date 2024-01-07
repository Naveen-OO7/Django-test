from django.db import models
from django.contrib.auth import models as auth_models


class User(auth_models.AbstractUser):
    """
    This model is for storing user table
    """

    login_count = models.IntegerField(default=0)
