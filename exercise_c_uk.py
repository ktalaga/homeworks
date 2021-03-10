united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
united_kingdom[1]["capital"] = "Cardiff"
print(united_kingdom[1]["capital"])
# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
northern_ireland = {
    "name": "Northern Ireland",
    "population": 1811000,
    "capital": "Belfast"
  }
united_kingdom.append(northern_ireland)
#print(united_kingdom)
# 3. Use a loop to print the names of all the countries in the UK.
names = united_kingdom[0]["name"], united_kingdom[1]["name"], united_kingdom[2]["name"], united_kingdom[3]["name"]
for name in names:
    print(name)
# 4. Use a loop to find the total population of the UK.
#populations = [{united_kingdom[0]["population"]}, {united_kingdom[1]["population"]}, {united_kingdom[2]["population"]}, {united_kingdom[3]["population"]}]
#print(populations)
populations = united_kingdom
# print(populations)
total_population = 0
for population in populations:
    total_population = total_population + population["population"]
print(total_population)
# check_total = 5295000 + 3063000 + 53010000 + 1811000
# print(check_total)