cities = tuple(input('Input some cities with space-bitween: ').split())
if 'moscow' in cities: print(cities)
else: cities = list(cities); cities.append('moscow'); cities = tuple(cities); print(cities)