from django.db import models


class Video(models.Model):
    aid = models.IntegerField()
    bvid = models.CharField(max_length=15)
    title = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return f'video_{self.aid}'
