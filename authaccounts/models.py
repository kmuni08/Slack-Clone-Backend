from django.db import models
from django.core.validators import MinLengthValidator


# # Create your models here.

# every field should have min length and pw shouldn't have min or max length.
# check if email field has @.

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(validators=[MinLengthValidator(5)], max_length=100, unique=True)  # username should be unique.
    email = models.CharField(validators=[MinLengthValidator(10)], max_length=100, unique=True)  # email must be unique.
    password = models.CharField(validators=[MinLengthValidator(10)], max_length=500, blank=True)
