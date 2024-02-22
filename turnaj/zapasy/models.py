from django.db import models

# Create your models here.
class Týmy(models.Model):
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    trener = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id}:{self.city} ({self.code})"
    
class Zápas(models.Model):
    tym_home = models.ForeignKey(Týmy, on_delete=models.CASCADE, related_name="home")
    tym_host = models.ForeignKey(Týmy, on_delete=models.CASCADE, related_name="host")
    vysledek = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.tym_home} -> {self.tym_host} : ({self.vysledek})"

