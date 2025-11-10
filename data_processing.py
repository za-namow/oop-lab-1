import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany

print("All cities in Germany:")
temps = []
for city in cities:
    if city['country'] == "Germany":
        temps.append(str(city['city']))
print(temps)
print()

# Print all cities in Spain with a temperature above 12°C

print("All cities in Spain with a temperature above 12°C")
temps = []
for city in cities:
    if city['country'] == "Spain":
        if float(city['temperature']) > 12:
            temps.append(str(city['city']))
print(temps)
print()

# Count the number of unique countries

print("Number of unique countries")
temps = []
for i in cities:
    if i["country"] not in temps:
        temps.append(i["country"])
l = len(temps)
print(l)
print()

# Print the average temperature for all the cities in Germany

print("Average temperature for all the cities in Germany")
count = 0
temps = 0
for city in cities:
    if city['country'] == "Germany":
        temps+=float(city['temperature'])
        count+=1
        temps=temps/count
print(temps)
print()

# Print the max temperature for all the cities in Italy

print("Max temperature for all the cities in Italy")
temps = 0
for city in cities:
    if city['country'] == "Italy":
        if float(city['temperature']) > temps:
            temps = float(city['temperature'])
print(temps)
