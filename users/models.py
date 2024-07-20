from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    ROLES = (
    ('team_owner', 'Team Owner'),
    ('admin', 'Team Admin'),
    ('member', 'Team Member'),
    )
    role = models.CharField(max_length=15, choices=ROLES,blank=True, null=True)
    username = models.CharField(max_length=150, unique=True,db_index=True) # Ensure username is indexed
    def is_ppms_or_superuser(self):
        return self.is_superuser or self.role == 'team_owner'
