# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 16:18:51 2021

@author: Giovanni Olivetti
"""

#%% UNIT TEST - pytest usage

# Instead of simply running the code on my shell and lose the results the next times
# I can start to compoand this in a more specific test

# for every functionality that my function is suppose to have I'll define a specific function
# that test that functionality and tells if the result is true or false

# there is an appropriate library, called pytest, that can help us...

# pytest is a command line program that:
# 1.	search all the current directory for each *.py files
# 2.	in each one of those, search all the functions named test_<something>
# 3.	execute all of them and keep track of the results (check if they end succesfully)
# 4.	prints a summary of the tests’ result


#key_not_found = object()

#def getitem(mapping, key):
 #   if key not in mapping:
  #      return key_not_found
   # return mapping[key]

#lista = {'a':1, 'b':2}

#assert getitem(lista, 'b') == 2;
#assert getitem(lista, 'a') == 1;


# after having installed pytest if you run it from spyder terminal (the command is
# !pytest name_of_the_file.py) it will return "no test run in 0.01 s".
# we need to define a programm and give the name test to the testing function in it

#%% 
# inside the test function I want to define everything I need to run the test!

#def test_return_correct_value():
 #   lista = {'a':1, 'b':2}
  #  assert getitem(lista, 'b') == 2; 
    
# now I can run the pytest function that will tell us how many mistakes are achieved

# NOTE that if I want to test more cases it's very important that each test is disconnetted 
# from each other
# if I want to test with a different key... I have to define a function with a new name, 
# even if is similar to the previous


#def test_return_correct_value_bis():
 #   lista = {'a':1, 'b':2}
  #  assert getitem(lista, 'a') == 1; 

# in this way they are completly independent

#NOTE: the number of dots that are written behaind the name of the function in the 
# output represents the number of tests passed (F is written when a test is not passed)

#%%
# let's change a bit the initial funciton

key_not_found = object()

def getitem(mapping,key):
    # return the key with the lowercase value, basically it means that:
    #     assert getitem(lista, 'b') == 2; it will be equal to
    #     assert getitem(lista, 'B') == 2; 
    # So I enlarge the possibilities of our inputs
    key = key.lower()
    print(key)
    for k, v in mapping.items():
        k = k.lower()
        print(k)
        if k == key:
            print(v)
            return v;
        #else:
        #    return key_not_found
    #return mapping[key]


# let's immagine the function is correctly defined
# which will be the test?

def test_return_corret_value_with_uppercase():
        lista = {"a":1, "b":2}
        assert getitem(lista, "A") == 1; 
        
# let's consider also the other possible test

def test_return_corret_value_with_uppercase_bis():
        lista = {"a":1, "b":2}
        assert getitem(lista, "B") == 2; 
        

# if instead I want that nothing changes between lower and upper case I should
# also test the case in which the dictionary uses upper case words and we test
# lower case keys as inputs..

  
def test_return_corret_value_with_uppercase_2():
        lista = {"A":1, "B":2}
        assert getitem(lista, "A") == 1; 
        
def test_return_corret_value_with_uppercase_2_bis():
        lista = {"A":1, "B":2}
        assert getitem(lista, "B") == 2; 
        
def test_return_corret_value_with_uppercase_3():
        lista = {"A":1, "B":2}
        assert getitem(lista, "a") == 1; 
        
def test_return_corret_value_with_uppercase_3_bis():
        lista = {"A":1, "B":2}
        assert getitem(lista, "b") == 2; 
    
# here I also copy the above tests

def test_return_correct_value():
    lista = {"a":1, "b":2}
    assert getitem(lista, "b") == 2; 
    
def test_return_correct_value_bis():
    lista = {"a":1, "b":2}
    assert getitem(lista, "a") == 1; 


#%% 
# if we want to add further difficoulties we can consider mixed cases


def test_mixed_case():
    lista = {"Primo":1, "Secondo" :2}
    #print(getitem(lista, "primo"))
    if getitem(lista, "primo") == 1:
        return True
'''EVEN IF THE OUTPUT IS TRUE THE pytest FUNCTION SAYS THIS TEST FAILS...'''
    
def test_mixed_case_2():
    lista = {"Primo":1, "Secondo" :2}
    assert getitem(lista, "PRIMO") == 1;
''' EVEN IF getitem(lista,"PRIMO") RETURNS 1, THE TEST FAILS AS IF THE ASSERTION IS FALSE '''
    
def test_mixed_case_3():
    lista = {"Primo":1, "Secondo" :2}
    assert getitem(lista, "secondo") == 2;
''' EVEN IF getitem(lista,"PRIMO") RETURNS 1, THE TEST FAILS AS IF THE ASSERTION IS FALSE '''
    
def test_mixed_case_4():
    lista = {"Primo":1, "Secondo" :2}
    assert getitem(lista, "SECONDO") == 2;
''' EVEN IF getitem(lista,"PRIMO") RETURNS 1, THE TEST FAILS AS IF THE ASSERTION IS FALSE '''









#%%
#first update version
def getitem(mapping,key):
    # return the key with the lowercase value, basically it means that:
    #     assert getitem(lista, 'b') == 2; it will be equal to
    #     assert getitem(lista, 'B') == 2; 
    # So I enlarge the possibilities of our inputs
    if key not in mapping:
        if key.isupper():
            key = key.lower()
            if key in mapping:
                return mapping[key]
            else:
                return key_not_found
        if key.islower():
            key = key.upper()
            if key in mapping:
                return mapping[key]
            else:
                return key_not_found
    else:
        return mapping[key]





