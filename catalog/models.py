from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name='like', blank=True)
    dislikes = models.ManyToManyField(User, related_name='dislike', blank=True)




def summary(self):
    return self.body[:100]


def pub_date_pretty(self):
    return self.pub_date.strftim('%b %e, %Y')


def __str__(self):
    return self.title
