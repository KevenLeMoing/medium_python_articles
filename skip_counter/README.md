# One minute, one tip

Everything you need to reproduce this article's results is available in this Github repository

### A basic logic: counting

Using a counter could be very useful when it comes to data engineering, from processing to exploratory analysis.
Managing a variable only for that purpose could decrease your code readability, or even worse if your logic needs many counter implementations.

### Goal
We would like to associate a counter with list of items without managing an additional variable.

### How it works ?
The function "count()" from "itertools" that will play the counter role (as an iterator).
This is the parameter passed to count() that allows the first item initialisation. The value is by default set at 0.

Indeed, our goal is to obtain the same results as below, without using the variable count.
```
cities = ['Madrid', 'London', 'Roma', 'Amsterdam', 'Stockholm']
counter = 1
cities_with_rank=[]

## Here we are using a counter to keep track of the item's rank
for item in ['Madrid', 'London', 'Roma', 'Amsterdam', 'Stockholm']:
    city = (item, my_counter)
    cities_with_rank.append(city)
    my_counter += 1

print(cities_with_rank)
```

Counting without variable

```
from itertools import count

## Counting item's rank without using any variable
for item in zip(count(1), my_list):
    city = (item[1], item[0])
    cities_with_rank.append(city)

print(cities_with_rank)
```


