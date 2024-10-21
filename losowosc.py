# Losowanie całkowitel liczby z przedziału 1-3
import random
x = random.randrange(1,3)
print(x)

# tablica
tab=[]
n=0
while n < 3:
    w = random.randrange(1, 4)
    tab.append(w)
    n = n+1
print (tab)