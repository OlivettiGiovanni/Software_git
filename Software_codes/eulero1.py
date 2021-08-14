#If we list all the natural numbers below 10 that are 
#multiples of 3 or 5, we get 3, 5, 6 and 9. 
#The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.


numbers = range(1,1000) #range(i,f,step)
s = 0

for number in numbers:
    if number%3 == 0 or number%5 == 0 :
        s = s + number
        
print(s)



#alternative

five = range(0,3,1000)
three = range(0,5,1000)

for number in five :
    s = s+ five
    
for number in three:
    s = s + three
    
print (s)

#l'alternativa non va bene in quanto somma
#più volte lo stesso numero

#we can substract the one counted two times

sum(range(0,1000,3)) + sum( range(0,1000,5)) - sum(range(0,1000,15))

#anyway il metodo più veloce è

sum (n for n in range(1000) if n%3 == 0 or n%5==0)
# sum(expression)
#the expression is typically a loop or anyway a condition
#which select a list of number to be summed

#professor solutions

def is_multiple(i,n):
    return i%n == 0

sum (i for i in range(1000) if is_multiple(i,3) or is_multiple(i,5))

