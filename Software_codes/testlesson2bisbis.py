# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 10:35:05 2021

@author: Giovanni Olivetti
"""

def _converter(k):
    if isinstance(k, str):
        return k.lower(k)
    else:
        return k
    
def getitem_old(mapping, key):
    # return the key with lower case value so tha
    # getitem(lista, "b") == getitem(lista, "B")
    key = _converter(key)
    lower_case = {_converter(k): v for k, v in mapping.items()}
    return lower_case[key]


#%% generalization in order to allow possible 
# modification of the function that is applied to both
# key and mapping.items
    
def getitem(mapping, key, transform=_converter):
    # return the key with lower case value so tha
    # getitem(lista, "b") == getitem(lista, "B")
    key = transform(key)
    lower_case = {transform(k): v for k, v in mapping.items()}
    return lower_case[key]

# I might give the user the chance to personalize this function
# I can do that by taking that function as an argument that has a default
# that is a function that transform my values...

# if, after that modification, pytest still pass all the tests I'm fine!
# the problem is that all the tests fails... maybe is because I did not
# specify the third argument of the new function getitem ?? 
# I copied the function of the professor and his tests are succesfull (same
# function and at least half of identical tests)
# I don't know how I should explicit the third argument...

# Considering that manually testing the behavioru some cases are correct 
# probably the tests fails for the structure of the function itself...

#%% testing

import pytest

def test_return_corret_value_with_uppercase_2():
        lista = {"A":1, "B":2}
        assert getitem(lista, "A") == 1; 
def test_return_corret_value_with_uppercase_2_bis():
        lista = {"A":1, "B":2}
        assert getitem(lista, "B",) == 2; 
        
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



def test_mixed_case():
    lista = {"Primo":1, "Secondo" :2}
    #print(getitem(lista, "primo"))
    if getitem(lista, "primo") == 1:
        return True
    
'''EVEN IF THE OUTPUT IS TRUE THE pytest FUNCTION SAYS THIS TEST FAILS...'''
    
def test_mixed_case_2():
    lista2 = {"Primo":1, "Secondo" :2}
    if getitem(lista2, "PRIMO") == 1:
        return True
''' EVEN IF getitem(lista,"PRIMO") RETURNS 1, THE TEST FAILS AS IF THE ASSERTION IS FALSE '''
    
def test_mixed_case_3():
    lista3 = {"Primo":1, "Secondo" :2}
    if getitem(lista3, "secondo") == 2:
        return True
''' EVEN IF getitem(lista,"PRIMO") RETURNS 1, THE TEST FAILS AS IF THE ASSERTION IS FALSE '''
    
def test_mixed_case_4():
   lista4 = {"Primo":1, "Secondo" :2}
   if getitem(lista4, "SECONDO") == 2:
        return True
''' EVEN IF getitem(lista,"PRIMO") RETURNS 1, THE TEST FAILS AS IF THE ASSERTION IS FALSE '''



def test_missing_key():
    lista = {"a" :1, "b" :2}
    with pytest.raises(KeyError):
        getitem(lista, "c")
        
def test_missing_key_bis():
    lista = {"1":1, "2":2}
    with pytest.raises(KeyError):
        getitem(lista, 1)
# this test shouldn't pass because we don't rise any keyerror considering
# we managed the code in order to accept a int key


# what if we have 1 as a string in the list and we insert as a key 1 as a number? 

# PERSONAL QUESTION: aren't we drammatically modifing the function for each test we perform? 
# wouldn't be more useful to avoid these tests and pretend that the user read the documentation. 
# if there is written to insert a string as a key, why someone should insert a integer?
# it would be maybe worst to not rise errors in these cases...

def test_numeric_key():
    listan = {"1":1,"2":2}
    if getitem(listan, 1) ==1:
        return True
    
def test_numeric_key_bis():
    lista = {1:1, 2:2}
    assert getitem(lista,"2") == 2

















