from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Story(models.Model):
    text = models.TextField()
    number = models.IntegerField()
    id = models.IntegerField()


class Story_part(models.Model,Story.id):
    text = models.CharField(max_length=140)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    story_id = Story.id

class Finished_story(models.Model):
    story = models.ForeignKey(Story.text, on_delete=models.CASCADE)
