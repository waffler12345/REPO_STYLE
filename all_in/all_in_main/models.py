from django.db import models

class TournamentParticipant(models.Model):
    # CharField refers to text
    name = models.CharField(max_length=127)
    # IntegerField refers to a number
    age = models.IntegerField()

class Shiba(models.Model):
    # CharField refers to text
    name = models.CharField(max_length=127)
    # IntegerField refers to a number
    age = models.IntegerField()

