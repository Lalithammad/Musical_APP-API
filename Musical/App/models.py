from django.db import models

# Create your models here.
class MusicModel(models.Model):
    title = models.CharField(max_length=150)
    contributors = models.CharField(max_length=200)
    iswc = models.CharField(max_length=50,unique=True)
    source = models.CharField(max_length=50)
    song = models.FileField()
    def __str__(self):
        return self.title

class ShowDataModel(models.Model):
    select = models.ForeignKey(MusicModel,on_delete=models.CASCADE)
