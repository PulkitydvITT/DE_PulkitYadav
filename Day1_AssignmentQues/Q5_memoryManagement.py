import gc

# in python everything is an object. when a value is assigned to a varaible, Python creates an object in memory and the variable becomes a reference to that object.

x = 10
#here python creates an integer object 10 in memory
#variable x points to the memory location of that object

#python uses dynamic typing, which means a variable can refer to different types of object at different times.
x = "Hello"
#now x points to an string object

#garbage collection
#python uses automatic garbage collection to free the memory. 
a = 5
del a
#now integer object 5 has no references , python frees the memory automatically

a = []
b = a
a.append(b)
#here it creates a circular reference , i.e: list references itself

gc.disable() #it will prevent automatic GC
gc.collect() #manually runs gc, frees the circular objects
