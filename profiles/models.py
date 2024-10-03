from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_wholesale = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class WholesaleProfile(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    tax_id = models.CharField(max_length=50)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name