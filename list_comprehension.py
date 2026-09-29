# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
# negative= [number for number in numbers if number <=0]
# print(negative)

# tuple_list = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]

# for t in tuple_list:
#     print(t)


# slope= lambda x1, x2, y1, y2: (y2 - y1) / (x2 - x1)
# print(slope(3,5,-2,-5))

# list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flatten=[i for row in list_of_lists for i in row]
# print(flatten)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened= [[country.upper(),country[:3].upper(), j.upper()] for i in countries for country, j in i]
print(flattened)

# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# list_of_dictionaries= [{"countri":countrie, "city": city} for item in countries for countrie,city in item ]
# print(list_of_dictionaries)

