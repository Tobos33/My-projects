import numpy as np
import tkinter as tk
from tkinter import ttk

r_0 = 1
E =  0.5
lamb = 0.12 # lamb = L**2 - 1

u_0 = -np.sqrt(2*E - lamb/r_0**2)

def f(r):
    u_dot = lamb/r**3
    return u_dot

def g(r):
    phi_dot = np.sqrt(lamb+1)/r**2
    return phi_dot

def runge_kutta_u( r, dt):
    k1_r = r
    k1 = f(k1_r)*dt

    k2_r = (r+k1/2)
    k2 = f(k2_r)*dt

    k3_r = (r+k2/2)
    k3 = f(k3_r)*dt

    k4_r = (r+k3)
    k4 = f(k4_r)*dt

    u = (1/6)*(k1+2*k2+2*k3+k4)
    return u

def runge_kutta_r(u , dt):
    k1 = u*dt

    k2 = (u+k1/2)*dt


    k3 = (u+k2/2)*dt


    k4 = (u+k3)*dt


    r = (1/6)*(k1+2*k2+2*k3+k4)
    return r


def runge_kutta_phi( r, dt):
    k1_r = r
    k1 = g(k1_r)*dt


    k2_r = (r+k1/2)
    k2 = g(k2_r)*dt

    k3_r = (r+k2/2)
    k3 = g(k3_r)*dt
    

    k4_r = (r+k3)
    k4 = g(k4_r)*dt
    

    phi = (1/6)*(k1+2*k2+2*k3+k4)
    return phi


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
x = r_0*np.cos(phi)
y = np.sin(phi)*r_0

for i in range(100001):
    #print(r, phi, u)
    t = (i)*dt
    T.append(t)
    U.append(u)
    R.append(r)
    PHI.append(phi)
    X.append(x)
    Y.append(y)


    phi += runge_kutta_phi(r, dt)
    u += runge_kutta_u( r, dt)
    r += runge_kutta_r( u, dt)

    y = r*np.sin(phi)
    x = r*np.cos(phi)

    if r <= 0.0:
        print(phi, u)
        break


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
with open("C:/Users/pawko/OneDrive/Pulpit/python/knfk/pytabela_runge-kutta.txt", "w") as file:
    file.write(latex_table)

#print("Tabela LaTeX została wygenerowana.")

'''root = tk.Tk()
root.title("Tabela")
columns = ("nr iteracji", "t (s)", "r", "phi")
tree = ttk.Treeview(root, columns=columns, show="headings", height = 17)

for col in columns:
    tree.heading(col, text=col)
for i in range(11):
    tree.insert("", tk.END, values=(i, round(T[i], 4), R[i], PHI[i]))
for i in range(6):
    tree.insert("", tk.END, values=((i+1)*10000, round(T[(i+1)*10000], 4), R[(i+1)*10000], PHI[(i+1)*10000]))



tree.pack()
root.mainloop()'''






