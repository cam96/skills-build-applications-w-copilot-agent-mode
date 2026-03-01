from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', members=['Iron Man', 'Captain America', 'Thor', 'Black Widow'])
        dc = Team.objects.create(name='dc', members=['Superman', 'Batman', 'Wonder Woman', 'Flash'])

        # Users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User(email='cap@marvel.com', name='Captain America', team='marvel'),
            User(email='thor@marvel.com', name='Thor', team='marvel'),
            User(email='widow@marvel.com', name='Black Widow', team='marvel'),
            User(email='superman@dc.com', name='Superman', team='dc'),
            User(email='batman@dc.com', name='Batman', team='dc'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='dc'),
            User(email='flash@dc.com', name='Flash', team='dc'),
        ]
        User.objects.bulk_create(users)

        # Activities
        activities = [
            Activity(user='Iron Man', type='run', duration=30, date='2023-01-01'),
            Activity(user='Captain America', type='cycle', duration=45, date='2023-01-02'),
            Activity(user='Thor', type='swim', duration=25, date='2023-01-03'),
            Activity(user='Black Widow', type='yoga', duration=60, date='2023-01-04'),
            Activity(user='Superman', type='run', duration=50, date='2023-01-01'),
            Activity(user='Batman', type='cycle', duration=40, date='2023-01-02'),
            Activity(user='Wonder Woman', type='swim', duration=35, date='2023-01-03'),
            Activity(user='Flash', type='yoga', duration=55, date='2023-01-04'),
        ]
        Activity.objects.bulk_create(activities)

        # Leaderboard
        Leaderboard.objects.create(team='marvel', points=150)
        Leaderboard.objects.create(team='dc', points=170)

        # Workouts
        workouts = [
            Workout(name='Pushups', description='Do 20 pushups', difficulty='easy'),
            Workout(name='Sprints', description='Run 5 sprints', difficulty='medium'),
            Workout(name='Plank', description='Hold plank for 2 minutes', difficulty='hard'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
