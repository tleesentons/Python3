# The while loop

a = 1
while a < 5:
    print(a)
    a += 1
    
# for loop 

for data in [1,2,3,4,5]:
    print(data)
    
    
for key,data in enumerate('string'):
    if key % 2 == 0: # Key is divided by 2 should equal zero than is even
        print('The letter {} is in an even location'.format(data))
        

tuple = (1,2,3,4,5)
for each in tuple:
    print(type(each),each)
    
    
tuple = (1,2,3,4,5)
try:
    tuple.append(6)
    for each in tuple:
        print(type(each),each)
except AttributeError as e: #e is used as error
    print('Error Formed:', e)
