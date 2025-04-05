import csv

def save_routes(routes, filepath):
    if not routes:
        return
    with open(filepath, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=routes[0].keys())
        writer.writeheader()
        writer.writerows(routes)
