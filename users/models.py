from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "user"

    # profile = models.OneToOneField(verbose_name="내프로필",on_delete=models.CASCADE,null=True,blank=True)
    

# class profile