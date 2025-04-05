from data_loader import load_routes, load_weather
from analyzer import filter_routes_by_length, avg_temperature, total_precipitation
from output_writer import save_routes

# Wczytaj dane
routes = load_routes('trasy.csv')
weather = load_weather('pogoda.csv')

# Filtrowanie tras od 5 do 10 km
filtered_routes = filter_routes_by_length(routes, 5, 10)

# Obliczenia pogodowe
avg_temp = avg_temperature(weather)
total_rain = total_precipitation(weather)

# Zapisz przefiltrowane trasy
save_routes(filtered_routes, 'wynik_trasy.csv')

# Wypisz statystyki pogodowe
print(f"Średnia temperatura: {avg_temp:.2f}°C")
print(f"Suma opadów: {total_rain:.2f} mm")
