from django.db import models
from django.contrib.auth.models import User

class Proctor(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

# email = models.EmailField(
#         max_length=50,
#         unique=True,
#         null=False,
#         blank=False,
#         validators=[RegexValidator(regex='^([a-z\d\.-]+)@bmsce.ac.in', message='Enter a valid email address.', code='invalid_email')]
#         )
