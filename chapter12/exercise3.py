'''Investigate the copy module. What does deepcopy do? In
which exercises from last chapter would deepcopy have come in handy?'''

'''A: copy.copy(x)
Return a shallow copy of x.
copy.deepcopy(x)
Return a deep copy of x. 
A shallow copy constructs a new compound object and then (to the extent possible) inserts references 
into it to the objects found in the original.
A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects 
found in the original.
The exercise about 
">>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> a == b
True
>>> a is b
False"
from last chapter would deepcopy have come in handy.
'''