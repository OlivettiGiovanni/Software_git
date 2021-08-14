# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 12:29:31 2021

@author: Giovanni Olivetti
"""

def getitem(mapping, key):
    #return 1
    return mapping[key]

#if the key does not exist??

#%%FIRST SKETCHES

def getitem(mapping, key):
    if key not in mapping:
        return None
    return mapping[key]

# none may be a not so good return value... instead we can return a specific object

#%%

key_not_found = object()

def getitem(mapping, key):
    if key not in mapping:
        return key_not_found
    return mapping[key]


#%%
# let's check further more what happend depending on the input we chose
# a dictionary defines a unique correspondance between some elements and a bounce of key values
# ex:
# month = { "Jan" : "January", "Feb" : "February",... }

# let's create a test dictionary
test = {'a':1, 'b':2}
getitem(test, 'b')
print(getitem(test, 'b'))
# yes, it's doing what it should do... but it's doing what it is intended to do HERE AND NOW
# Tomorrow could be different and how can I remember which where the result of the previous run?


#%% INFORMAL TEST

# let's consider the so colled informal test --> low level of usefulness
if __name__ == "__main__":
    getitem(test, 'b')
    getitem(test, 'a')
    
# the condition check if the programm is run as a script directly or if it's recalled 
# by another script. In the first case the condition is satisfied.


#%%
# how can I improve it?
# I can also add what I expect they result

if __name__ == "__main__":
    getitem(test, 'b') == 2;
    getitem(test, 'a') == 1;
    #print(getitem(test, 'b') == 2)
    #print(getitem(test, 'a') == 2)   

# in this way the output can be true or false

#%%
#an alternative using the assert is
if __name__ == "__main__":
    assert getitem(test, 'b') == 2;
    assert getitem(test, 'a') == 1;
# the output will tell something only if the assertion returns an error

#anyway... this is the first step in the direction of unit testing 



#%%  UNIT TEST (to be continued..)
# Instead of simply running the code on my shell and lose the results the next times
# I can start to compoand this in a more specific test

# for every functionality that my function is suppose to have I'll define a specific function
# that test that functionality and tells if the result is true or false

# there is an appropriate library, called pytest, that can help us...
# let's discuss about that in the next file.






