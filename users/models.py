from django.contrib.auth.models import AbstractUser, UserManager as basic_userManager


class UserManager(basic_userManager):
    '''https://github.com/django/django/blob/master/django/contrib/auth/models.py#L131'''
    def _create_user(self, username, email, password, **extra_fields):
        return super()._create_user(usrname, email,password, **extra_fields)

    def create_user(self,username, email=None, password=None, **extra_fields):
        super().create_user(username,email,password,**extra_fields)


class User(AbstractUser):
    '''https://github.com/django/django/blob/master/django/contrib/auth/models.py#L288'''
    object = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
