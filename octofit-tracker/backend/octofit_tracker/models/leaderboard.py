from djongo import models

class Leaderboard(models.Model):
    _id = models.ObjectIdField()
    team = models.CharField(max_length=50)
    points = models.IntegerField()
    rank = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'

    def __str__(self):
        return f"{self.team} - {self.points}"
