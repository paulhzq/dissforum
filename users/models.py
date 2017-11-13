from django.contrib.auth.models import AbstractUser

class UserManager():
    '''https://github.com/django/django/blob/master/django/contrib/auth/models.py#L131'''
    pass

class User(AbstractUser):
    '''https://github.com/django/django/blob/master/django/contrib/auth/models.py#L288'''
    object = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
