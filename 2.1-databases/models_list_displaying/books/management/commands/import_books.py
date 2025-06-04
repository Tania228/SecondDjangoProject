import json
from django.core.management.base import BaseCommand
from books.models import Book


class Command(BaseCommand):
    help = 'Импортирует информацию о книгах из json-файла'

    def add_arguments(self, parser):
        parser.add_argument(
            'json_file',
            type=str,
            help='Путь к json-файлу с данными и книгах'
        )

    def handle(self, *args, **options):
        json_file = options['json_file']

        with open(json_file, encoding='utf-8') as file:
            books = json.load(file)

        for book in books:
            name = book['fields']['name']
            author = book['fields']['author']
            pub_date = book['fields']['pub_date']

            Book.objects.create(
                name=name,
                author=author,
                pub_date=pub_date
            )

        self.stdout.write(self.style.SUCCENSS('Информация о книгах успешно импортирована'))