import csv
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    help = 'Import phones from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']

        with open(csv_file_path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')  # Указываем разделитель ";"
            for row in reader:
                if 'name' not in row:
                    self.stderr.write(self.style.ERROR(f'Ошибка: В файле {csv_file_path} нет колонки "name"'))
                    return

                phone = Phone(
                    name=row['name'].strip(),
                    price=float(row['price']),
                    image=row['image'].strip(),
                    release_date=row['release_date'].strip(),
                    lte_exists=row['lte_exists'].strip().lower() in ['1', 'true', 'yes']
                )
                phone.save()
                self.stdout.write(self.style.SUCCESS(f'Добавлен телефон: {phone.name}'))


