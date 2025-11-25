from django.core.management.base import BaseCommand
from django.conf import settings

from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Populating octofit_db with test data...'))
        client = MongoClient('mongodb://localhost:27017/')
        db = client['octofit_db']
        db.drop_collection('users')
        db.drop_collection('teams')
        db.drop_collection('activities')
        db.drop_collection('leaderboard')
        db.drop_collection('workouts')

        # Teams
        teams = [
            {'name': 'Marvel', 'description': 'Team Marvel Superheroes'},
            {'name': 'DC', 'description': 'Team DC Superheroes'},
        ]
        db.teams.insert_many(teams)

        # Users
        users = [
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team': 'Marvel'},
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': 'Marvel'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': 'DC'},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': 'DC'},
        ]
        db.users.insert_many(users)
        db.users.create_index([('email', 1)], unique=True)

        # Activities
        activities = [
            {'user': 'spiderman@marvel.com', 'activity': 'Running', 'duration': 30},
            {'user': 'ironman@marvel.com', 'activity': 'Cycling', 'duration': 45},
            {'user': 'wonderwoman@dc.com', 'activity': 'Swimming', 'duration': 60},
            {'user': 'batman@dc.com', 'activity': 'Yoga', 'duration': 20},
        ]
        db.activities.insert_many(activities)

        # Workouts
        workouts = [
            {'name': 'Morning Cardio', 'suggested_for': 'Marvel'},
            {'name': 'Strength Training', 'suggested_for': 'DC'},
        ]
        db.workouts.insert_many(workouts)

        # Leaderboard
        leaderboard = [
            {'user': 'spiderman@marvel.com', 'points': 100},
            {'user': 'ironman@marvel.com', 'points': 90},
            {'user': 'wonderwoman@dc.com', 'points': 110},
            {'user': 'batman@dc.com', 'points': 95},
        ]
        db.leaderboard.insert_many(leaderboard)

        self.stdout.write(self.style.SUCCESS('octofit_db populated successfully!'))
