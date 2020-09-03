# 1) Aşağıdaki String'in 5. harfini my_letter isimli bir değişkene atayınız.

my_string = "James Hetfield"
my_letter = my_string[4]
print(my_letter)

# Aşağıdaki String'in 5. ve 8. karakteri arasındaki tüm harflerini yazdırınız (5 ve 8 dahil)

my_new_string = "QuentinTarantino"
print(my_new_string[4:8])

# Aşağıdaki String'i kod ile tersten yazın

my_last_string = "Afyonkarahisarlılaştıramadıklarımızdanmısınız"
print(my_last_string[::-1])

# 1) Aşağıdaki işlemin sonucu hangi veri tipinde olacaktır?

my_sum = 3 + 10.2 + 50

print(my_sum)
print(type(my_sum))

# 2) Aşağıdaki işlemin sonucu kaçtır?

my_sum2 = 5 + 8 * 12

print(my_sum2)

# 1) Bu listeyi 3 farklı yoldan oluşturunuz: [1,2,"a"]

my_list = [1,2,"a"]
print(type(my_list))

my_set = {1,2,"a"}
print(type(my_set))

my_dictionary = {"k1":1,"k2":2,"k3":"a"}
print(type(my_dictionary))

# 2) Aşağıdaki "a"'yı tek satırda alınız:
my_list = [1,4,[2,3,"a"]]
print(my_list[2][2])

# 3) Aşağıdaki "b"'yi tek satırda alınız:

my_dictionary = {"k1":2, "kk":[4,{"kkkk":"b"}]}
print(my_dictionary["kk"][1]["kkkk"])

# 4) Aşağıdaki liste set'e çevirilince hangi değerler içinde kalacaktır?

my_list_to_be_set = [11,12,22,33,11,22,45,32,21,22,33,45]
my_set = set(my_list_to_be_set)
print(type(my_set))

# 1) Aşağıdaki ifadenin sonucu ne olacaktır?

x = 40 * 5 + 3
y = 208 - 2 * 4
print(x>y)

# 2) Aşağıdaki ifadenin sonucu ne olacaktır?

a = 40 * (4 - 2)
b = 80 - 2 * -5
print(a>b)



