from functools import reduce

# Filtrowanie tras wg długości, trudności i regionu
def filter_routes(routes, min_len=None, max_len=None, difficulty=None, region=None):
    return list(filter(lambda r: (
        (min_len is None or float(r['length_km']) >= min_len) and
        (max_len is None or float(r['length_km']) <= max_len) and
        (difficulty is None or int(r['difficulty']) == difficulty) and
        (region is None or r['region'] == region)
    ), routes))

# Średnia temperatura
def avg_temperature(weather_data):
    temps = [float(d['avg_temp']) for d in weather_data]
    return sum(temps) / len(temps) if temps else 0

# Suma opadów
def total_precipitation(weather_data):
    return reduce(lambda acc, d: acc + float(d['precipitation']), weather_data, 0)

# Liczba dni słonecznych (np. sunshine_hours > 8)
def count_sunny_days(weather_data, threshold=8):
    return len(list(filter(lambda d: float(d['sunshine_hours']) > threshold, weather_data)))
