from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} profile.'.format(self.user.username)


def create_profile(sender, **kwarg):
    if kwarg['created']:
        user_profile = Profile.objects.create(user=kwarg['instance'])


post_save.connect(create_profile, sender=User)
