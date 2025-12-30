import random

rand_list = [random.choice(range(1, 21)) for i in range(20)]

list_comprehension_below_10 = [x for x in rand_list if x<10]

list_comprehension_below_10 = list(filter(lambda x: x<10, rand_list))