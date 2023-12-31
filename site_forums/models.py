from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=2000)

    def __str__(self):
        return(f'{ self.title } by { self.username }.')
    
class LoginUser(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return(f'{ self.username }')
    
class Comment(models.Model):
    content = models.CharField(max_length=2000)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    commented_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return(f'{ self.username.username } on { self.post.title }')
    
class Reply(models.Model):
    comment = models.ForeignKey(Comment, related_name='replies', on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    replied_at = models.DateTimeField(auto_now_add=True)
    reply = models.TextField()

    def __str__(self):
        return self.username.username

    @property
    def get_replies(self):
        return self.replies.all()
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return(f'{ self.user.username }')
    
### Music Page ###

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
    upload_date = models.DateTimeField(auto_now_add=True)
    audio_file = models.FileField(upload_to='audio/')

    def __str__(self):
        return f'{self.title} by {self.artist}'