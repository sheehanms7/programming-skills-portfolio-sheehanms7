rivers = {'Yamuna': 'Ganga',
          'Amazon': 'Brazil',
          'Mekong': 'Thailand'
          }

for river, country in rivers.items():
    print(f"The {river} runs through the {country}.")

print ("\nRivers:")
for river in rivers.keys():
    print (river)

print ("\nCountries")
for country in rivers.values():
    print (country)