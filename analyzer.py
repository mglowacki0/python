from functools import reduce

def filter_routes_by_length(routes, min_km, max_km):
    return list(filter(lambda r: min_km <= float(r['length_km']) <= max_km, routes))

def avg_temperature(weather_data):
    temps = list(map(lambda d: float(d['avg_temp']), weather_data))
    return sum(temps) / len(temps) if temps else 0

def total_precipitation(weather_data):
    return reduce(lambda acc, d: acc + float(d['precipitation']), weather_data, 0)
