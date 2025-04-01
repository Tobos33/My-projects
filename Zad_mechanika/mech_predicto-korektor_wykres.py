import matplotlib.pyplot as plt
import numpy as np

r_0 = 1
E =  0.3
lamb = 0.12 # lamb = L**2 - 1
phi_0 = 0

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
phi = phi_0
dphi = 0
x = r_0*np.cos(phi)
y = np.sin(phi)*r_0

for i in range(100001):
    T.append(t)
    U.append(u)
    R.append(r)
    PHI.append(phi)
    X.append(x)
    Y.append(y)

    t = i*dt
    phi += (1/2)*(g(r+g(r)*dt)+g(r))*dt
    u += (1/2)*(f(r+f(r)*dt)+f(r))*dt
    r +=(1/2)*(U[i]+ U[i]*dt +U[i])*dt

    y = r*np.sin(phi)
    x = r*np.cos(phi)


plt.grid(True)
plt.plot(T, R)
plt.title(f"Wykres r(t) wykonany metodą predictor-corector \n dla E={E}, lambda^2={lamb}, r0={r_0}, phi0={phi_0}, u0={round(u_0,1)}")
plt.xlabel('t (s)')
plt.ylabel('r')
plt.savefig("C:/Users/pawko/OneDrive/Pulpit/python/knfk/p-k_pokazr(t).png")
plt.show()
#plt.plot(T, U)
#plt.show()
plt.grid(True)
plt.plot(PHI, R)
plt.title(f"Wykres r(phi) wykonany metodą predictor-corector \n dla E={E}, lambda^2={lamb}, r0={r_0}, phi0={phi_0}, u0={round(u_0,1)}")
plt.xlabel('phi')
plt.ylabel('r')
plt.savefig("C:/Users/pawko/OneDrive/Pulpit/python/knfk/p-k_pokazr(p).png")
plt.show()
#plt.plot(R, PHI)
#plt.title(f"Wykres r(phi) wykonany metodą predictor corector \n dla E={E}, lambda^2={lamb}, r0={r_0}, phi0={phi_0}, u0={round(u_0,1)}")
#plt.xlabel('r')
#plt.ylabel('phi')
#plt.show()
plt.grid(True)
plt.plot(T, PHI)
plt.title(f"Wykres phi(t) wykonany metodą predictor-corector \n dla E={E}, lambda^2={lamb}, r0={r_0}, phi0={phi_0}, u0={round(u_0,1)}")
plt.xlabel('t (s)')
plt.ylabel('phi')
plt.savefig("C:/Users/pawko/OneDrive/Pulpit/python/knfk/p-k_pokazp(t).png")
plt.show()
plt.scatter(0, 0, color = 'r')
plt.plot(X, Y)
plt.title(f"Zmiana położenia punktu materialnego \n wykonana metodą predictor-corector \n dla E={E}, lambda^2={lamb}, r0={r_0}, phi0={phi_0}, u0={round(u_0,1)}")
plt.xlabel('x')
plt.ylabel('y')
plt.savefig("C:/Users/pawko/OneDrive/Pulpit/python/knfk/p-k_pokazxy.png")
#plt.xlim(-5, 5)
#plt.ylim(-5, 5)
plt.show()
