from django.db import models
from django.contrib.auth.models import User
from account.models import Profile
from django.urls import reverse
from django.utils.text import slugify
from tinymce import models as tinymce_models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    statuses = [
        ("D", "Draft"),
        ("P", "Published"),
    ]
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True,blank=True)
    content = tinymce_models.HTMLField()
    status = models.CharField(max_length=1, choices=statuses)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="blog/post", blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})

    def update_reverse_path(self):
        return reverse('update-blog', kwargs={'slug': self.slug})

    def delete_reverse_path(self):
        return reverse('delete-blog', kwargs={'slug': self.slug})

