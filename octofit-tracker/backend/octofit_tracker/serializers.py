from rest_framework import serializers
from octofit_tracker.models.user import User
from octofit_tracker.models.team import Team
from octofit_tracker.models.activity import Activity
from octofit_tracker.models.leaderboard import Leaderboard
from octofit_tracker.models.workout import Workout


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['_id', 'name', 'email', 'team', 'is_superhero']
        read_only_fields = ['_id']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['_id', 'name', 'description']
        read_only_fields = ['_id']


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['_id', 'user', 'type', 'duration', 'calories', 'date']
        read_only_fields = ['_id']


class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = ['_id', 'team', 'points', 'rank']
        read_only_fields = ['_id']


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['_id', 'name', 'description', 'difficulty', 'duration']
        read_only_fields = ['_id']
