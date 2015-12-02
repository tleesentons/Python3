#switch similar to if is not build in to python
switch = dict(
        one = 'one',
        two = 'two',
        three = 'three'
)
var = 'four'

#print(switch[var])
print(switch.get(var,'default'))