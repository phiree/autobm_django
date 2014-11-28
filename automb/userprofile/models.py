from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User)
    real_name=models.CharField(max_length=20,null=True,blank=True,verbose_name='真实姓名')
    gender_choice=(('m','男'),('f','女'))
    gender=models.CharField(max_length=2,choices=gender_choice,default=gender_choice[0][0],verbose_name='性别')
    phone=models.CharField(max_length=200,null=True,verbose_name='电话号码')
    email=models.EmailField(max_length=100,null=True,blank=True,verbose_name='电子邮件')
User.profile=property(lambda u:UserProfile.objects.get_or_create(user=u)[0])