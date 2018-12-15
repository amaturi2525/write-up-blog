from django.db import models


# Create your models here.
class Problem(models.Model):
    class Meta:
        db_table  = 'problem'
    title = models.CharField(max_length=255)
    ctf = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title


