from djongo import models

class Activity(models.Model):
    _id = models.ObjectIdField()
    user = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # minutes
    calories = models.IntegerField()
    date = models.DateField()
    class Meta:
        db_table = 'activities'

    def __str__(self):
        return f"{self.user} - {self.type}"
