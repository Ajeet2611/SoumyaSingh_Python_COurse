 #tuples Basics
 
myTuples = (78,90,75)
studentTuples =("ravi",22,"btech","ajeet","mca","rahul",24,"mba")
print("myTuples =", myTuples)
print("studentTuples =", studentTuples)
print("length of myTuples =", len(myTuples))
print("length of studentTuples =", len(studentTuples))
print("accessing element 0 of myTuples =", myTuples[0])
print("accessing element 1 of studentTuples =", studentTuples[1])


#empty tuple
empty_tuple = ()
print("empty_tuple =", empty_tuple)
print("length of empty_tuple =", len(empty_tuple))
print("type of empty_tuple =", type(empty_tuple))


singleTuple = (42,)#couma is necessary for single element tuple
print("singleTuple =", singleTuple)
print("length of singleTuple =", len(singleTuple))
print("type of singleTuple =", type(singleTuple))
print("find ajeet in studentTuples at index =", studentTuples.index("ajeet"))
print("count of ajeet in studentTuples =", studentTuples.count("ajeet"))