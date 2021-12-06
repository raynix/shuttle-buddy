import re

from django.db import models
from datetime import datetime

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
    ticket_price = models.IntegerField(default=12)

    @classmethod
    def get_next_game(cls, last_game, delta_days=7):
        new_game = cls()
        new_game.name = last_game.name
        new_game.venue = last_game.venue
        new_game.date = last_game.date + datetime.timedelta(days=delta_days)
        new_game.time = last_game.time
        new_game.ticket_price = last_game.ticket_price
        new_game.courts.set(last_game.courts.all())
        return new_game

    @classmethod
    def find_game(cls, message):
        try:
            match = re.search(r'^(.+) on (.+) at (.+)', message)
            game_name = match.group(1)
            game_date = match.group(2)
            game_time = match.group(3)

            game = cls.objects.get(name=game_name, date=game_date, time=game_time)
            return game
        except:
            return None

    def __str__(self):
        return f"{self.name} on {self.date} at {self.time}"

    def get_max_layers(self):
        return sum([court.max_players for court in self.courts.all()])

class Player(models.Model):
    username = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.username} ({self.firstname} {self.lastname})"

class Booking(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    social_game = models.ForeignKey(SocialGame, on_delete=models.CASCADE)
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    def __str__(self):
        return f"{self.player} in {self.social_game}"