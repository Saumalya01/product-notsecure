from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from django.utils.crypto import get_random_string

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20)
    api_key = models.CharField(max_length=20, unique=True, blank=True)
    
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to.'),
        related_name="customuser_groups",
        related_query_name="customuser",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="customuser_permissions",
        related_query_name="customuser",
    )

    def save(self, *args, **kwargs):
        if not self.api_key:
            self.api_key = get_random_string(20)
        super().save(*args, **kwargs)