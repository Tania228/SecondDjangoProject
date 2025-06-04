import csv
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from phones.models import Phone


class Command(BaseCommand):
    help = 'Импортирует информацию о телефонах из csv-файла'

    def add_arguments(self, parser):
        parser.add_argument(
            'csv_file',
            type=str,
            help='Путь к csv-файлу с данными о телефонах'
        )

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        with open(csv_file, 'r', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            slug = slugify(phone['name'])

            Phone.objects.create(
                id=phone['id'],
                name=phone['name'],
                image=phone['image'],
                price=phone['price'],
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists'],
                slug=slug
            )

            self.stdout.write(self.style.SUCCESS('Информация о телефонах успешно импортирована!'))



