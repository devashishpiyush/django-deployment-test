from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class UserProfileManager(BaseUserManager):
    """Manager for the UserProfile."""
    def create_user(self, email, first_name, last_name, password=None):
        """Create and return a new user profile."""
        if not email:
            raise ValueError('User must have an email id.')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password):
        """Create and return a new super user profile."""
        user = self.create_user(email, first_name, last_name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for the users."""
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        """Return string representation of the UserProfile."""
        return self.email

    def get_full_name(self):
        """Return full name of the user."""
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        """Return short name / first name of the user."""
        return self.first_name
