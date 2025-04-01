import matplotlib.pyplot as plt
import numpy as np

r_0 = 1
E =  0.5
lamb = 0.12 # lamb = L**2 - 1

u_0 = -np.sqrt(2*E - lamb/r_0**2)
#print(u_0)
def f(r):
    u_dot = lamb/r**3
    return u_dot

def g(r):
    phi_dot = np.sqrt(lamb+1)/r**2
    return phi_dot


T = []
R = []
U = []
PHI = []
X = []
Y = []
dt = 0.0001
t = 0
r = r_0
u = u_0
phi = 0
dphi = 0
x = r_0*np.cos(phi)
y = np.sin(phi)*r_0

for i in range(100001):
    t = i*dt
    T.append(t)
    U.append(u)
    R.append(r)
    PHI.append(phi)
    X.append(x)
    Y.append(y)


    phi += (1/2)*(g(r+g(r)*dt)+g(r))*dt
    u += (1/2)*(f(r+f(r)*dt)+f(r))*dt
    r +=(1/2)*(U[i]+ U[i]*dt +U[i])*dt

    y = r*np.sin(phi)
    x = r*np.cos(phi)



tab = []
for i in range(11):
    tab.append([i, round(T[i], 4), R[i], PHI[i]])

for i in range(10):
    tab.append([(i+1)*10000, round(T[(i+1)*10000], 4), R[(i+1)*10000], PHI[(i+1)*10000]])

latex_table = "\\begin{tabular}{|l|l|l|l|}\n\\hline\n"
latex_table +="nr iteracji & t (s) & r & phi \\\\\n\\hline\n"
for i in tab:
    for j in tab[tab.index(i)]:
        if tab[tab.index(i)].index(j) == 0:
            row_text = str(j)  # Konwertuj każdy element wiersza do stringa
            latex_table += row_text
        else:
            row_text = " & " + str(j)  # Konwertuj każdy element wiersza do stringa
            latex_table += row_text
    latex_table += " \\\\\n\\hline\n"
latex_table += "\\end{tabular}"

# Zapis do pliku
with open("C:/Users/pawko/OneDrive/Pulpit/python/knfk/pytabela_predictor-korektor.txt", "w") as file:
    file.write(latex_table)
