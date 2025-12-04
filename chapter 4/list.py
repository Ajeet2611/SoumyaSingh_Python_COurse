#creating a list in python

#my favorite fruits print and access elements only string value store
my_Favorite_fruits = ["apple", "banana", "cherry", "date"]
print(my_Favorite_fruits)
print(my_Favorite_fruits[2])#accessing cherry
print(my_Favorite_fruits[-1])#accessing date
print(my_Favorite_fruits[-2])#accessing cherry == my_Favorite_fruits[2]
print(my_Favorite_fruits[0])#accessing apple
print(my_Favorite_fruits[1])#accessing banana
print(my_Favorite_fruits[1:3])# accessing banana and cherry
print(my_Favorite_fruits[:3])# accessing apple, banana and cherry
print(my_Favorite_fruits[2:])# accessing cherry and date
print(len(my_Favorite_fruits))#length of list

#list with mixed data types
print ("-----list with mixed data types-----")
mixed_list = ["hello", 42, 3.14, True]
print(mixed_list)#printing entire list
print(mixed_list[0])#accessing hello
print(mixed_list[1])#accessing 42
print(mixed_list[2])#accessing 3.14
print(mixed_list[3])#accessing True
print("leanth is list = ",len(mixed_list))#length of mixed list

#changed indexing value
print("-----changed indexing value-----")
mixed_list[0] = "hi"
print(mixed_list)#printing entire list after changing first element
mixed_list[2] = 2.71
print(mixed_list)#printing entire list after changing third element

