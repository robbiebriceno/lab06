from django.db import models
from django.contrib.auth.models import User
from news.models import Category, Article

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    dark_mode = models.BooleanField(default=False)
    favorite_articles = models.ManyToManyField(Article, blank=True, related_name="favorited_by")
    subscribed_categories = models.ManyToManyField(Category, blank=True, related_name="subscribers")

    def __str__(self):
        return f"{self.user.username}'s Profile"