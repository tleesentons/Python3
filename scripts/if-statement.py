# If Statement with comparison == != > < >= <= or and if elif else
a,b = 0,1
if a == b:
    print(True)
elif a < 1:
    print('a is less than b')
else:  
    print(False)
if a != b:
    print(True)
if a < b or a != b:
    print('Both or True')
if a >= b:
    print(True)
if a < b and a != b:
    print('Both and True')
    
print(True if a == b else False)

a = 1
b = 0
c = 1

if(b == 1):
    bHolder = 0
elif(b==0):
    bHolder = 1
    
if(a == 1 and bHolder == 1):
    firstBracketHolder = 1
else:
    firstBracketHolder = 0
if(firstBracketHolder == 1 or c == 1):
    print('Q = 1')
else:
    print('Q = 0')