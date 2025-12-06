  #Dictionary create
student={
    "name":"ajeet",
    "age":21,
    "City":"Patna",
    "rollno":444,
    "name":"Ravi",  #duplicate key, last one will be considered
    "name":"Ankit"  #duplicate key, last one will be considered
}

print(type(student))
print(student["name"])  #Ravi
print(student["name"])  #Ankit
print("my dictionory item is :  ",student) #{'name': 'Ankit', 'age': 21, 'City': 'Patna', 'rollno': 444}
print(student["age"])
print(student["City"])  #Patna
student["City"] = "Hydrabad"
print("updated city is : ",student["City"])  #Hydrabad

student["favorite_subject"] = "Maths"  #adding new key value pair
print("updated dictionory is : ",student)  #{'name': 'Ankit', 'age': 21, 'City': 'Hydrabad', 'rollno': 444, 'favorite_subject': 'Maths'}

student.pop("favorite_subject")  #removing key value pair
print("after removing favorite subject : ",student)  #{'name': 'Ankit',
student.keys()  #getting all keys
student.values()  #getting all values
student.items()  #getting all items
print("all keys are : ",student.keys())
print("all values are : ",student.values())
print("all items are : ",student.items())
print("length of dictionory is : ",len(student))  #4
print("get method : ",student.get("name"))  #Ankit
print("get method : ",student.get("favorite_subject"))  #None
print("update method : ",student.update({"age":22,"City":"Delhi"}))  #updating multiple key value pair
print("after update dictionory is : ",student)  #{'name': 'Ankit', 'age': 22, 'City': 'Delhi', '

