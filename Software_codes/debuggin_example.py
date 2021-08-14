# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 19:31:02 2021

@author: Giovanni Olivetti
"""

def calculator():
    par = input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division")
    inp1 = float(input("Enter the first value: "))
    inp2 = float(input("Enter the second value: "))
    result_c = 0;   # I need that to reference a variable before assignment.
    if par == 1:
        result_c = inp1 + inp2;
    elif par == 2:
        result_c = inp1 - inp2;
    elif par == 3:
        result_c = inp1 * inp2;
    elif par == 4:
        result_c = inp1 / inp2;
    #print(result_c);
    return result_c  
