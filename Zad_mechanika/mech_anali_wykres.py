import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0 , 10, 0.0001)

r_0 = 1
E =  0.3
lamb = 0.12 # lamb = L**2 - 1
phi_0 = 0
C = np.sqrt(2*E*r_0**2-lamb)
L = np.sqrt(lamb+1)
p = (C-2*E*t)/np.sqrt(lamb)


r = +np.sqrt((4*E**2*t**2 - 4*E*C*t+2*E*r_0**2)/(2*E))
phi = -(L/np.sqrt(lamb))*np.arctan(p) +(L/np.sqrt(lamb))*np.arctan(C/np.sqrt(lamb))
y = np.sin(phi)*r
x = np.cos(phi)*r

plt.grid(True)
plt.plot(t, r)
plt.title(f"Wykres r(t) wykonany metodą analityczną \n dla E={E}, lambda^2={lamb}, r0={r_0}, phi0={phi[0]}")
plt.xlabel('t (s)')
plt.ylabel('r')
plt.savefig("C:/Users/pawko/OneDrive/Pulpit/python/knfk/anali_pokaz3r(t).png")
plt.show()
#plt.plot(T, U)
#plt.show()
plt.grid(True)
plt.plot(phi, r)
plt.title(f"Wykres r(phi) wykonany metodą analityczną \n dla E={E}, lambda^2={lamb}, r0={r_0}, phi0={phi[0]}")
plt.xlabel('phi')
plt.ylabel('r')
#plt.savefig("C:/Users/pawko/OneDrive/Pulpit/python/knfk/anali_pokaz3r(p).png")
plt.show()
#plt.plot(R, PHI)
#plt.title(f"Wykres r(phi) wykonany metodą predictor corector \n dla E={E}, lambda^2={lamb}, r0={r_0}, phi0={phi_0}, u0={round(u_0,1)}")
#plt.xlabel('r')
#plt.ylabel('phi')
#plt.show()
plt.grid(True)
plt.plot(t, phi)
plt.title(f"Wykres phi(t) wykonany metodą analityczną \n dla E={E}, lambda^2={lamb}, r0={r_0}, phi0={phi[0]}")
plt.xlabel('t (s)')
plt.ylabel('phi')
#plt.savefig("C:/Users/pawko/OneDrive/Pulpit/python/knfk/anali_pokaz3p(t).png")
plt.show()
plt.scatter(0, 0, color = 'r')
plt.plot(x, y)
plt.title(f"Zmiana położenia punktu materialnego \n wykonana metodą analityczną \n dla E={E}, lambda^2={lamb}, r0={r_0}, phi0={phi[0]}")
plt.xlabel('phi')
plt.ylabel('r')
#plt.savefig("C:/Users/pawko/OneDrive/Pulpit/python/knfk/anali_pokaz3xy.png")
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.show()

