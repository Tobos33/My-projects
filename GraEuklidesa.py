i = 0
t = int(input("podaj liczbę partii: "))
liczby = []
for i in range(t):
    a = 101
    b = 101
    while(a and b > 100):
        a = int(input(f"podaj liczbę żetonów gracza 1 w {i+1} partii: "))
        b = int(input(f"podaj liczbę żetonów gracza 2 w {i+1} partii: "))    
        if (a and b > 100):
            print("Za duże liczby podaj je jeszcze raz")
    liczby += [a, b]
j = 0
l = 0
for j in range(t):
    while ( liczby[l] != liczby[l + 1]):   
        if liczby[l] < liczby[l + 1]:
            liczby[l + 1] -= liczby[l]
        elif liczby[l] > liczby[l + 1]:
            liczby[l] -= liczby[l + 1]
    print("liczba żetonów: " + str(liczby[l]*2))
    l += 2

    

