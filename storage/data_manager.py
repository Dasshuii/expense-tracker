import csv

DATA_PATH = './storage/expenses.csv'

expenses = []

def load_expenses():
    with open(DATA_PATH, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            expenses.append(row)
    return expenses

def write_expense():
    with open(DATA_PATH, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([4, '2025-07-06', 'Veterinary', 100])