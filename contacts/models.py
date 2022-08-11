from django.db import models
from django.conf import settings

# Create your models here.
class Contact(models.Model):
    """Database model for the contacts in the address book."""


    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )


    GENDER_LIST = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=255, null=True)
    phone = models.CharField(max_length=10, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_LIST)
    dob = models.DateField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender']

    def __str__(self):
        """Return string representation of Contact"""
        return f'{self.first_name} {self.last_name}'
