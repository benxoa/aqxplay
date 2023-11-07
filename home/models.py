from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self) -> str:
        return self.name


class Publish(models.Model):
    class Meta:
        verbose_name = "Publish"
        verbose_name_plural = "Publishes"
    
    # Making publish model
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    
    title = models.CharField(max_length=77)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to="uploads/",null=False,blank=False)
    description = models.TextField()
    date = models.DateTimeField(
        auto_now=True)
    
    def __str__(self) -> str:
        return self.title
