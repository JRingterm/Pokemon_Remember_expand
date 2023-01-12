from django.contrib.auth.base_user import BaseUserManager
#from django.utils.translation import ugettext_lazy as _ 더이상 사용 x

#User모델에서 username대신 email을 사용할 계획. 
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields): #일반유저 생성
        #이메일과 password로 계정만듦.
        if not email: #이메일을
            raise ValueError('이메일은 필수입력요소입니다')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields): #슈퍼유저 생성
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)