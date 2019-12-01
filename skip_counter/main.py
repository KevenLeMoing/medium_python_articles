from itertools import count

cities = ['Madrid', 'London', 'Roma', 'Amsterdam', 'Stockholm']
counter = 1


def count_with_var(my_list: list, my_counter: int) -> dict:
    """Loop over a list to find the rank of each item"""
    cities_with_rank=[]
    for item in my_list:
        city = (item, my_counter)
        cities_with_rank.append(city)
        my_counter += 1
    return cities_with_rank


def count_without_var(my_list: list) -> dict:
    """Loop over a list to find the rank of each item"""
    cities_with_rank=[]
    for item in zip(count(1), my_list):
        city = (item[1], item[0])
        cities_with_rank.append(city)
    return cities_with_rank


assert count_with_var(my_list=cities, my_counter=counter) == count_without_var(my_list=cities)

print('-----------------------count by using a variable------------------------------')
print(count_with_var(my_list=cities, my_counter=counter))
print('-----------------------count without using a variable-------------------------')
print(count_without_var(my_list=cities))