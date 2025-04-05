import csv

def load_routes(filepath):
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

def load_weather(filepath):
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return [row for row in reader]
