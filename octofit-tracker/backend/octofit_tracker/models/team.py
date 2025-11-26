from djongo import models

class Team(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name
