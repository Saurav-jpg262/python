countries = ["Nepal","Korea","Japan","India"]
print("second country:", countries[1])
countries.append("China")
removed_country = countries.pop(0)
for country in countries:
    print(country)