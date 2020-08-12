from django.db import models

# Create your models here.

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}

        for user in User.objects.all():
            if user.username == postData['username']:
                errors['name_unavailable'] = 'That username is unavailable'

        return errors

class User(models.Model):
    username = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    objects = UserManager()

    def __repr__(self):
        return f'User: {self.username}'
