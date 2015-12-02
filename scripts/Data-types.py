#Two type of numbers intergent and float
#Float have decimal
#You can control the variable by typing int or foat at the variable or round
from tkinter.test.runtktests import this_dir_path
a = int(50.0) 
print(type(a),a) 
a = round(50.9) 
print(type(a),a)

x = '''
    This is 
    a string
'''

print(x)

b='Hello'
c='This is %s a string' %b
print(c)

y = 'Alex'
z = 'Joe'
t = "Welcome, {}". format(y)
print(t)