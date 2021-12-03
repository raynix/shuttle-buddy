from django.db import models

class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    google_map_url = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Court(models.Model):
    name = models.CharField(max_length=100)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    max_players = models.IntegerField(default=6)

    def __str__(self):
        return self.name

class SocialGame(models.Model):
    name = models.CharField(max_length=100)
    courts = models.ManyToManyField(Court)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    def __str__(self):
        return str(self.date) + " " + str(self.time) + " " + self.name

    def get_max_layers(self):
        return sum([court.max_players for court in self.courts.all()])