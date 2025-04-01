print("Kalkulator liczb- wpisz najpierw liczbę, później znak działania, a następnie drugą liczbę")
a = input("pierwsza liczba: ")
c = input("znak działania: ")
b = input("druga liczba: ")
if c != "+" and c != "-" and c != "/" and c != "*":
    print("należy umieścić znak działania (+ , - , * , /)")  
elif c == "/" and b == "0":
    print("nie można dzielić przez zero")
else:
    try:
        if c == "+":
            print(float(a)+float(b))
        elif c == "-":
            print(float(a)-float(b))
        elif c == "/":
            print(float(a)/float(b))
        elif c =="*":
            print(float(a)*float(b))
    except ValueError:
       print("Nie można wykonywać działań na znakackh")