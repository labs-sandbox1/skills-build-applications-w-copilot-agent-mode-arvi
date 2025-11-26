from django.core.management.base import BaseCommand
from octofit_tracker.models import user, team, activity, leaderboard, workout
from djongo import models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        user.User.objects.all().delete()
        team.Team.objects.all().delete()
        activity.Activity.objects.all().delete()
        leaderboard.Leaderboard.objects.all().delete()
        workout.Workout.objects.all().delete()

        # Create teams
        marvel = team.Team.objects.create(name='Marvel')
        dc = team.Team.objects.create(name='DC')

        # Create users
        users = [
            user.User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            user.User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            user.User.objects.create(name='Batman', email='batman@dc.com', team=dc),
            user.User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]

        # Create activities
        activities = [
            activity.Activity.objects.create(user=users[0], type='Running', duration=30),
            activity.Activity.objects.create(user=users[1], type='Cycling', duration=45),
            activity.Activity.objects.create(user=users[2], type='Swimming', duration=60),
            activity.Activity.objects.create(user=users[3], type='Yoga', duration=50),
        ]

        # Create workouts
        workouts = [
            workout.Workout.objects.create(name='Cardio Blast', description='High intensity cardio workout'),
            workout.Workout.objects.create(name='Strength Training', description='Build muscle strength'),
        ]

        # Create leaderboard
        leaderboard.Leaderboard.objects.create(team=marvel, points=100)
        leaderboard.Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
