continents = [
  {
    "name": "Asia",
    "countries": [{
        "name": "China",
        "population": 1439323776,
    }, {
        "name": "India",
        "population": 1380004385,
    }, {
        "name": "Japan",
        "population": 126476461,
    }]
  }, 
  {
    "name": "Europe",
    "countries": [{
        "name": "France",
        "population": 67067967,
    }, {
        "name": "Germany",
        "population": 83783942,
    }, {
        "name": "United Kingdom",
        "population": 67886011,
    }]
}]
for continent in continents:
    print(f"continent: {continent['name']}")
    for country in continent["countries"]:
        print(country["name"])