import csv

from django.core.management.base import BaseCommand

from accounts.models import Profile
from articles.models import Article, Tag


class Command(BaseCommand):
    help = 'Import articles from CSV file'

    def add_arguments(self, parser):  # noqa
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    # Get author profile
                    author = Profile.objects.get(
                        user__username=row['author_username']
                    )

                    # Create article
                    article, created = Article.objects.get_or_create(
                        author=author,
                        title=row['title'],
                        defaults={
                            'resume': row['resume'],
                            'content': row['content'],
                        },
                    )

                    # Add tags
                    if row['tags']:
                        tag_names = [
                            name.strip() for name in row['tags'].split(',')
                        ]
                        for tag_name in tag_names:
                            tag, _ = Tag.objects.get_or_create(name=tag_name)
                            article.tags.add(tag)

                    if created:
                        self.stdout.write(
                            self.style.SUCCESS(
                                f'Successfully created article: {article.title}'  # noqa
                            )
                        )
                    else:
                        self.stdout.write(
                            self.style.WARNING(
                                f'Article already exists: {article.title}'
                            )
                        )

                except Profile.DoesNotExist:
                    self.stdout.write(
                        self.style.ERROR(
                            f'Profile not found: {row["author_username"]}'
                        )
                    )
