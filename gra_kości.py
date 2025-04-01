from random import randint

lista = [randint(1,6),randint(1,6),randint(1,6),randint(1,6),randint(1,6),randint(1,6)]
lista2 = [randint(1,6),randint(1,6),randint(1,6),randint(1,6),randint(1,6),randint(1,6)]
i = 1
l = 1
suma1 = 0
suma2 = 0

for j in range(len(lista)):
    suma1 = suma1 + lista[j]

for k in range(len(lista2)):
    suma2 = suma2 + lista2[k]

print("twoje kości: " + str(lista))
print("suma twoich kości: " + str(suma1))
print("kości przeciwnika: " + str(lista2))
print("suma kości przeciwnika: " + str(suma2))


while i == 1:
    
        
    c = 0
    a = input("Czy chcesz rzucić jeszcze raz? (Tak/Nie)")

    if a == "Tak":
        
        while l == 1:   
            b = input("ile kości chcez zmienić") 
            if b == "1":
                c = input("jaką kość chcesz zmienić")

                lista[int(c) -1 ] = randint(1, 6)    
                
                i = 0
                l = 0
            elif b == "2":
                print("jakie kości chcesz zmienić(podaj numery w oddzielnych wierszach)")
                c = input()
                d = input()

                lista[int(c) - 1] = randint(1, 6)
                lista[int(d) - 1] = randint(1, 6)    
                
                i = 0
                l = 0
            elif b == "3":
                print("jakie kości chcesz zmienić(podaj numery w oddzielnych wierszach)")
                c = input()
                d = input()
                e = input()

                lista[int(c) - 1] = randint(1, 6)
                lista[int(d) - 1] = randint(1, 6)
                lista[int(e) - 1] = randint(1, 6) 
                
                i = 0
                l = 0
            elif b == "4":
                print("jakie kości chcesz zmienić(podaj numery w oddzielnych wierszach)")
                c = input()
                d = input()
                e = input()
                f = input()

                lista[int(c) - 1] = randint(1, 6)
                lista[int(d) - 1] = randint(1, 6)
                lista[int(e) - 1] = randint(1, 6)
                lista[int(f) - 1] = randint(1, 6)      
                
                i = 0
                l = 0
            elif b == "5":
                print("jakie kości chcesz zmienić(podaj numery w oddzielnych wierszach)")
                c = input()
                d = input()
                e = input()
                f = input()
                g = input()

                lista[int(c) - 1] = randint(1, 6)
                lista[int(d) - 1] = randint(1, 6)
                lista[int(e) - 1] = randint(1, 6)
                lista[int(f) - 1] = randint(1, 6)
                lista[int(g) - 1] = randint(1, 6)        
                
                i = 0 
                l = 0           
            elif b == "6":
                    
                lista[0] = randint(1, 6)   
                lista[1] = randint(1, 6)
                lista[2] = randint(1, 6)
                lista[3] = randint(1, 6)
                lista[4] = randint(1, 6)        
                lista[5] = randint(1, 6)   
                print(lista)
                i = 0
                l = 0 
            else:
                print("spróbuj jeszcze raz")
                l = 1 
    elif a == "Nie":
        i = 0
    else:
        print("spróbuj jeszcze raz")
        i = 1



if lista2[0] <= 3:
    lista2[0] = randint(1,6)
if lista2[1] <= 3:
    lista2[1] = randint(1,6)
if lista2[2] <= 3:
    lista2[2] = randint(1,6)
if lista2[3] <= 3:
    lista2[3] = randint(1,6)
if lista2[4] <= 3:
    lista2[4] = randint(1,6)
if lista2[5] <= 3:
    lista2[5] = randint(1,6)

suma1 = 0
suma2 = 0
for j in range(len(lista)):
    suma1 = suma1 + lista[j]

for k in range(len(lista2)):
    suma2 = suma2 + lista2[k]

print("twoje oto twoje oczka po kolejnym rzucie")
print(lista)
print("suma twoich oczek: " + str(suma1))

print("twój przeciwnik też rzucił ponownie, oto jego oczka")
print(lista2)
print("suma oczek przeciwnika: " + str(suma2))

if suma1 > suma2:
    print("wygrałeś")
    
elif suma1 < suma2:         
    print("przegrałeś")

elif suma1 == suma2:
    print("remis")
    