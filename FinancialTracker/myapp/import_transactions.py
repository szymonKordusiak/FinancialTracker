# import_books.py
import csv
from datetime import datetime
from myapp.models import Transactions

def import_books(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Transactions.objects.create(
                transaction_amount = row['Kwota'],
                transaction_location = row['Lokalizacja'],
                additional_information = row['Dodatkowe informacje'],
                transaction_date = row['Data waluty'],
            )

if __name__ == '__main__':
    csv_file_path = 'path/to/books.csv'  # Replace with your actual file path
    import_books(csv_file_path) # as