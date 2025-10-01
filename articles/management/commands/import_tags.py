import csv

from django.core.management.base import BaseCommand

from articles.models import Tag


class Command(BaseCommand):
    help = 'Import tags from CSV file'

    def add_arguments(self, parser):  # noqa
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                tag, created = Tag.objects.get_or_create(name=row['name'])
                if created:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'Successfully created tag: {tag.name}'
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f'Tag already exists: {tag.name}')
                    )
