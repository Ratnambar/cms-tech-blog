from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.urls import reverse,reverse_lazy

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=20, db_index=True, default="Add your name")
    bio = models.CharField(max_length=500, db_index=True, default="Add your information")
    image = models.ImageField(upload_to="profile/", db_index=True, default='profile/default.jpg')

    def __str__(self):
        return self.user.username

    def update_profile_reverse_path(self):
        return reverse('ProfileUpdate', kwargs={'pk': self.pk})

