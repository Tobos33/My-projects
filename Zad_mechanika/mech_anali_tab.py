import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0 , 10.0001, 0.0001)

r_0 = 1
E =  0.5
lamb = 0.12
C = np.sqrt(2*E*r_0**2-lamb)
L = np.sqrt(lamb+1)
p = (C-2*E*t)/np.sqrt(lamb)


r = np.sqrt((4*E**2*t**2 - 4*E*C*t+2*E*r_0**2)/(2*E))
phi = -(L/np.sqrt(lamb))*np.arctan(p) +(L/np.sqrt(lamb))*np.arctan(C/np.sqrt(lamb))
y = np.sin(phi)*r
x = np.cos(phi)*r

tab = []
for i in range(11):
    tab.append([i, round(t[i], 4), r[i], phi[i]])

for i in range(10):
    tab.append([(i+1)*10000, round(t[(i+1)*10000], 4), r[(i+1)*10000], phi[(i+1)*10000]])

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
with open("C:/Users/pawko/OneDrive/Pulpit/python/knfk/pytabela_analitycznie.txt", "w") as file:
    file.write(latex_table)