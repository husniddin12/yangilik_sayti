
from django.db import models
from django.urls import reverse
from django.utils.datetime_safe import datetime


class Category(models.Model):

    nomi = models.CharField(max_length=50)

    def __str__(self):
        return self.nomi


class PublishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = News.Status.Publish)



class News(models.Model):

    class Status(models.TextChoices):
        Draft = 'DR', "Darft"
        Publish = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_time = models.DateTimeField(auto_now=datetime.now)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=2, choices=Status.choices, default=Status.Draft)

    published = PublishManager()
    object = models.Manager()


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['published_time']

    def get_absolute_url(self):
        return reverse('deatil_link', kwargs={'slug': self.slug})



class Contact(models.Model):

    user = models.CharField(max_length=150)
    email = models.EmailField()
    msg = models.TextField()

    def __str__(self):
        return self.user
