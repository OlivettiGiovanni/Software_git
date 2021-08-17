# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 18:06:30 2021

@author: Giovanni Olivetti
"""

# testlesson2.py code with professor solution

def getitem_old(mapping, key):
    if type(key) == int:
        key = str(key)
    key = key.lower()
    lower_case = {k.lower() : v for k, v in mapping.items()}
    return lower_case[key]
    
#this last row means that if key is not in mapping the output will be an error


#%% testing
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



#%% 
# test for missing key
import pytest

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


#%%
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
    assert getitem(lista, "2") ==2

    
#%%
#• a more complete function that treat identically int and str input
def getitem(mapping, key):
    for k, v in mapping.items():
        if type(key) == int and type(k) == int:
            continue
        else: 
            break
    for k, v in mapping.items():      
        if type(key) == str and type(k) == str:
            key = key.lower()
            lower_case = {k.lower() : v for k, v in mapping.items()}
        else: 
            break
        return lower_case[key]   
    for k, v in mapping.items(): 
        if type(key) == str and type(k) == int:
            key = int(key)
        else:
            break
            break
    for k, v in mapping.items(): 
        if type(key) == int and type(k) == str:     
            key = str(key)
        else: 
            break
    return mapping[key]
    

    
    
    
    
    
    