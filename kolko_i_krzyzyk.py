import random
def wiersz ():
        while True:
            try:
                wp = int(input("Podaj numer wiersza od 1 do 3: "))
                if 1 <= wp <= 3:
                    return wp
                else:
                    print("Nie ma takiego wiersza.")
            except ValueError:
                print("Proszę podać liczbę całkowitą.")


def kolumna():
    while True:
        try:
            kp = int(input("Podaj numer kolumny od 1 do 3: "))
            if 1 <= kp <= 3:
                return kp
            else:
                print("Nie ma takiej kolumny.")
        except ValueError:
            print("Proszę podać liczbę całkowitą.")


def wprowadzanie_x (tab):
    while True:
        w = wiersz() - 1
        k = kolumna() - 1
        if tab[w][k] == " ":
            tab[w][k] = "X"
            break
        else:
            print("Te pole jest już zajęte. Wybierz inne.")



def wprowadzanie_o (tab):
    while True:
        w = random.randrange(0,3)
        k = random.randrange(0,3)
        print (w,k)
        if tab[w][k] == " ":
            tab[w][k] = "O"
            break


def wyswietlanie(tab):
    i=0
    while i<3:
        print(tab[i])
        i=i+1

def sprawdzenie (tab):
    g=0
    h=0
    #sprawdzenie wierszy
    while g < 3:
        if tab[g][0] == tab[g][1] == tab[g][2] == "X":
            print("Wygrał X!")
            exit()

        if tab[g][0] == tab[g][1] == tab[g][2] == "O":
            print("Wygrał O!")
            exit()

        g = g + 1

    # sprawdzenie po kolumnie
    while h < 3:
        if tab[0][h] == tab[1][h] == tab[2][h] == "X":
            print("Wygrał X!")
            exit()

        if tab[0][h] == tab[1][h] == tab[2][h] == "O":
            print("Wygrał O!")
            exit()

        h = h + 1
    # sprawdzenie po przekatnej
    if tab[0][0] == tab[1][1] == tab[2][2] == "X":
        print("Wygrał X!")
        exit ()

    if tab[0][0] == tab[1][1] == tab[2][2] == "O":
        print("Wygrał O!")
        exit()

    if tab[0][2] == tab[1][1] == tab[2][0] == "X":
        print("Wygrał X!")
        exit()

    if tab[0][2] == tab[1][1] == tab[2][0] == "O":
        print("Wygrał O!")
        exit ()



def puste_pola(tab):
    return any(" " in row for row in tab)

# tablica do gry 3x3
tab = [[" ", " " ," "], [" ", " " ," "],[" ", " " ," "]]
i = 0
while i < 3:
    print(tab[i])
    i = i + 1

# gra
while puste_pola(tab):
    wprowadzanie_x(tab)
    wyswietlanie(tab)
    sprawdzenie(tab)
    print ("Teraz komputer")
    wprowadzanie_o(tab)
    wyswietlanie(tab)
    sprawdzenie(tab)




