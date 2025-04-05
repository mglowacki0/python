from data_loader import load_csv_data
from analyzer import filter_routes, avg_temperature, total_precipitation, count_sunny_days
from output_writer import save_to_csv

# Wczytaj dane
routes = load_csv_data('trasy.csv')
weather = load_csv_data('pogoda.csv')

# Filtruj trasy: długość 5–15 km, trudność 2, region "Tatry"
filtered = filter_routes(routes, min_len=5, max_len=15, difficulty=2, region="Tatry")

# Analiza pogody
avg_temp = avg_temperature(weather)
sum_rain = total_precipitation(weather)
sunny_days = count_sunny_days(weather)

# Zapisz wyniki
save_to_csv(filtered, 'wynik_trasy.csv')

# Wyświetl podsumowanie
print(f"Znaleziono {len(filtered)} tras spełniających kryteria.")
print(f"Średnia temperatura: {avg_temp:.2f}°C")
print(f"Suma opadów: {sum_rain:.2f} mm")
print(f"Liczba dni słonecznych: {sunny_days}")
