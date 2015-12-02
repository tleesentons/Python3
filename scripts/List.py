from _collections_abc import ItemsView
x = [1,2,3,4,5] # square brackets used for list and () brackets used for "tuple"
x.append(6)
print(type(x),x[3:]) #you can add the index number the index start as 0

#dictionary used with { }
z = {'one': 1, 'two': 2}
print(type(z),z)

dictionary = dict(
                  one = 1,
                  two = 'two'
                  )
print(type(dictionary),dictionary)

#BOOLEAN is True or False
boolean = False
print(type(boolean),boolean)

#bool = True
a,b = 0,1
if a == b:
    print(True)
else:
    print(False)
#print(type(bool),bool)
print(a,b)

#In detail

list = [1,2,3,4,5,6,7,8,9,10,11,'two']
print(list[-3])
length = len(list)
print(list[length-3]) #Same as [-3] first method is preffered
print(list[1:5])
print(list[2:10:2]) #Stepper start at index 2 and skip 2 and run up to 9)

list.append(12)    #How to append the list
list2 = [12,13,14]

list.extend(list2) #How to extend the list

list.insert(5,22) #insert (index,item)
list[6] = 25 #another method of inserting
list[7] = list[7] * 2
del list[1:5]
list.remove('two')
list.reverse()
list.append(0)
list.reverse()
list.sort()
print(list)