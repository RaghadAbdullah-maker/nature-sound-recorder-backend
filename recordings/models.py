from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    
    
    def __str__(self):
        return self.name


class Recording(models.Model):
    
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    audio_file=models.FileField(upload_to='sounds/')
    created_at=models.DateTimeField(auto_now_add=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)

    
    
    def __str__(self):
        return self.title
    
    
    
    
class Favorite(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recording = models.ForeignKey(Recording,on_delete=models.CASCADE)

    
    
    class Meta:
        unique_together = ('user' , 'recording')
        
    def __str__(self):
        return f"{self.user.username} ❤️ {self.recording.title}"