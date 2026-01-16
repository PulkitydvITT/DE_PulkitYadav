import gc
x = 10
y = x
#10 is an object in an memory
#x points to 10
#y = x , y point to same object 

x = 20
#python creates a new object in memory
# x now points to 20
#y still points to 10

a = [1,2,3]
b = a
b.append(4)
#lists are mutable , so changes affect all references , so appending from b also affects a

#python variables are references, not actual copies
#immutable objects (int , string, tuple) creates a new object on change
# mutable objects (list, dictionary, set) shares memory among references 

x = []
y = x
x.append(y)
#now here circular reference created, python can't handle it by alone reference count, so garabage collector will handle this type of memory, we can also do it manually
gc.collect() #manually collect unreachable objects 