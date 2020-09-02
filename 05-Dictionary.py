
my_dictionary = {"key": "value"}
print(my_dictionary["key"])

my_fitness_dictionary = {"run": 100, "swim":200}
print(my_fitness_dictionary["run"])

my_dictionary_2 = {"k1":1,"k2":2,"k3":"apple"}
print(my_dictionary_2["k3"])

my_dictionary_3 = {"k1":100,20:30}
print(my_dictionary_3[20])

my_dictionary_4 = {"k1":100,"k2":[1,2,3],"k3":{"a":4}}
print(my_dictionary_4)

print(my_dictionary_4.keys())
print(my_dictionary_4.values())

print(my_dictionary_4["k3"]["a"])

my_dictionary_5= {"k1":3,"k2":2}
my_dictionary_5["k1"] = 10 
print(my_dictionary_5)
my_dictionary_5["k3"] = 7
print(my_dictionary_5)