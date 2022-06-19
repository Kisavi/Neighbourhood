from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

HOODS = (
    ('Kahawa Sukari', 'Kahawa Sukari'),
    ('Kahawa West', 'Kahawa West'),
    ('Kasarani', 'Kasarani')
)


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    bio = models.TextField(max_length=300)
    photo = CloudinaryField('image',
                            default='http://res.cloudinary.com/dim8pysls/image/upload/v1639001486/x3mgnqmbi73lten4ewzv.png')
    hood = models.CharField(choices=HOODS, max_length=25, default=1)

    def __str__(self):
        return self.bio


class Post(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=700)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description


class Comment(models.Model):
    commentor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    comment = models.TextField(max_length=300)

    def __str__(self):
        return self.comment
