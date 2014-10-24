from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User)
    phone=models.CharField(max_length=200,null=True)

User.profile=property(lambda u:UserProfile.objects.get_or_create(user=u)[0])