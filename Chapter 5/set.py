language ={"pythone","java","c++","javascript","ruby","html","css","sql","swift","go","kotlin","pythone","java"}
print(type(language))  #<class 'set'>
print("my set item is :  ",language)  #set items will be in unordered manner and no duplicate item will be there
#adding and removing item from set
language.add("R")  #adding new item to set
print("after adding new item my set is : ",language)
print("length of set is : ",len(language))  #length of set
language.remove("html")  #removing item from set
print("after removing item my set is : ",language)
language.discard("css")  #removing item from set
print("after discarding item my set is : ",language)
print("length of set is : ",len(language))  #length of set


#empty set creation
empty_set = set()
print(type(empty_set))  #<class 'set'>