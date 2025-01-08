from django.contrib.auth.models import AbstractUser
from django.db import models


class Tournament(models.Model):
    name = models.CharField(max_length=255, unique=True)
    info = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Commentator(AbstractUser):
    years_of_experience = models.IntegerField(null=True)

    class Meta:
        verbose_name = "commentator"
        verbose_name_plural = "commentators"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Match(models.Model):
    title = models.CharField(max_length=255)
    match_date = models.DateField(blank=True, null=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    commentators = models.ManyToManyField(Commentator, related_name="matches")

    def __str__(self):
        return self.title
