countries = input().split(', ')
capitals = input().split(', ')
pairs = {country: capital for country, capital in zip(countries, capitals)}
for country, capital in pairs.items():
    print(f'{country} -> {capital}')
