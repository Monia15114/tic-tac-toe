print("abcd","ala")
x=1

# petla while
while x<=5:
    print(x)
    x=x+1

# wprowadzanie danych i okreslanie liczby znaków
name = input(" Podaj imie:  ")
print ('Czesc ', name)
l=len(name)
print ("Liczba liter w twoim imieniu to", l)
z0=name[0]
z1=name[1]
z2=name[2]
print(z0)
print(z1)
print(z2)

# warunek if / else
zp=name[-1]
if zp == "a":
    print ('Jesteś kobietą')
else:
    print ('Nie jesteś kobietą')

# tablica
tab = []
n = 0
while n < l:
    tab.append(name[n])
    n=n+1
print(tab)

#zmiana znaku o jeden w alfabecie
a = input("Podaj literkę: ")
b = int(input ("Podaj cyfrę: "))
c = ord(a)
d = c+b
e = chr(d)
print("Litera o ", b, " dalej w alfabecie to: ", e)