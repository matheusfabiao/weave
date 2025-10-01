import csv
from datetime import datetime

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from accounts.models import Profile


class Command(BaseCommand):
    help = 'Import profiles from CSV file'

    def add_arguments(self, parser):  # noqa
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Create User
                user, created = User.objects.get_or_create(
                    username=row['username'],
                    defaults={
                        'email': row['email'],
                        'first_name': row['first_name'],
                        'last_name': row['last_name'],
                    },
                )
                if created:
                    user.set_password(row['password'])
                    user.save()

                # Create or update Profile
                profile, profile_created = Profile.objects.get_or_create(
                    user=user,
                    defaults={
                        'bio': row['bio'],
                        'location': row['location'],
                        'phone': row['phone'],
                        'birth_date': datetime.strptime(
                            row['birth_date'], '%Y-%m-%d'
                        ).date()
                        if row['birth_date']
                        else None,
                    },
                )

                if not profile_created:
                    profile.bio = row['bio']
                    profile.location = row['location']
                    profile.phone = row['phone']
                    profile.birth_date = (
                        datetime.strptime(row['birth_date'], '%Y-%m-%d').date()
                        if row['birth_date']
                        else None
                    )
                    profile.save()

                self.stdout.write(
                    self.style.SUCCESS(
                        f'Successfully imported {user.username}'
                    )
                )
