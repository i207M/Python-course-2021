from django.db import models


class Up(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    face = models.CharField(max_length=80)
    sign = models.TextField()
    num_fan = models.IntegerField()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f'up_{self.id}'
