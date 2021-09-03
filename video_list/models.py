from django.db import models


class Video(models.Model):
    aid = models.IntegerField(unique=True)
    bvid = models.CharField(max_length=15)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    cover = models.CharField(max_length=80)
    num_view = models.IntegerField()
    num_like = models.IntegerField()
    num_coin = models.IntegerField()
    num_favorite = models.IntegerField()
    up_id = models.IntegerField()
    up_name = models.CharField(max_length=40)
    up_face = models.CharField(max_length=80)
    upload_time = models.CharField(max_length=20)
    reply = models.JSONField()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f'video_{self.aid}'
