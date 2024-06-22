from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=30)
    
    
    def __str__(self):
        return self.name
    
class User(AbstractUser):
    home_adress = models.TextField(unique=True, blank=True, null=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'home_adress']
    def __str__(self):
        return self.username
    
class Complain(models.Model):
    written_by = models.ForeignKey(User, on_delete=models.CASCADE)
    written_at = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    image = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.content
    
class Answer(models.Model):
    answer_to_compl = models.ForeignKey(Complain, on_delete=models.CASCADE)
    answer_content = models.TextField()
    answer_date = models.DateTimeField(default=timezone.now)
    is_accepted = models.BooleanField()

# Create your models here.
