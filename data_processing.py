import csv, os

# __location__ = os.path.realpath(
#     os.path.join(os.getcwd(), os.path.dirname(__file__)))

# cities = []
# with open(os.path.join(__location__, 'Cities.csv')) as f:
#     rows = csv.DictReader(f)
#     for r in rows:
#         cities.append(dict(r))

# # Print first 5 cities only
# for city in cities[:5]:
#     print(city)

class DataLoader:
    pass

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
average_temp = (lambda cities: sum(map(lambda x: float(x['temperature']), cities)) / len(cities))
print(average_temp(cities))
print()

# Print all cities in Germany

print("All cities in Germany:")
print(list(map(lambda x: x['city'], filter(lambda x: x['country'] == 'Germany', cities))))
print()


# Print all cities in Spain with a temperature above 12°C

print("All cities in Spain with a temperature above 12°C")
print(list(map(lambda x: x['city'], filter(lambda x: x['country'] == 'Spain' and float(x['temperature']) > 12, cities))))
print()


# Count the number of unique countries

print("Number of unique countries")
print(len(set(map(lambda x: x['country'], cities))))
print()


# Print the average temperature for all the cities in Germany

print("Average temperature for all the cities in Germany")

get_avg = lambda data: sum(data) / len(data) if data else 0
germany_temps = list(map(lambda x: float(x['temperature']),filter(lambda x: x['country'] == 'Germany', cities)))

print(get_avg(germany_temps))
print()


# Print the max temperature for all the cities in Italy

print("Max temperature for all the cities in Italy")

italy_temps = list(map(lambda x: float(x['temperature']),filter(lambda x: x['country'] == 'Italy', cities)))

get_max = lambda data: max(data) if data else None
print(get_max(italy_temps))
print()
