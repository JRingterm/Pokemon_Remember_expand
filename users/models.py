from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.utils.translation import ugettext_lazy as _ :2.2버전 이상부터는 더이상 사용 x
from .managers import CustomUserManager

# Django에서 제공하는 기본 User모델은 username이 필수이기 때문에, AbstractUser를 상속받아 이메일만 사용할 수 있도록 커스터마이징했다.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    spouse_name = models.CharField(blank=True, max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.email
