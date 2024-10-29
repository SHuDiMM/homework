from random import random, Random

my_dict = {"Sergei":1992, "Gosha":1975, "Andrei":2001 }
print("Dict:",my_dict)
print("Existing value:",my_dict.get("Sergei"),"\n"+"Not existing value:", my_dict.get("Kuzma"))
my_dict.update({'Dmitry':1990, 'Roman':1655})
removed_element = my_dict.pop('Gosha')
print("Deleted value:", removed_element)
print("Modified dictionary:", my_dict)
print()
my_set = {2,2,2,0.7,0.9,3.4,3.4,0.7,'Monitor', 'Weekend', ("синий", "зеленый", "красный"),'Monitor' }
print("Set:", my_set)
my_set.add("Mouse")
my_set.add(4.8)
my_set.discard(Random)
print("Modified set:", my_set)

