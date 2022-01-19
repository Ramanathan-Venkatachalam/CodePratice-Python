#Dictionary in a List
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country_name, visits_name, cities_name):
  new_country = {}
  new_country["country"] = country_name
  new_country["visits"] = visits_name
  new_country["cities"] = cities_name
  travel_log.append(new_country)

add_new_country("India", 20, ["Chennai", "Mumbai"])
print(travel_log)



