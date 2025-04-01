import numpy as np
import matplotlib.pyplot as plt

r_0 = 1
E = 0
lamb = -0.25 # lamb = L**2 - 1
phi_0 = 0
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
phi = phi_0
dphi = 0
x = r_0*np.cos(phi)
y = np.sin(phi)*r_0

for i in range(100000):
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

plt.grid(True)
plt.plot(T, R)
plt.title(f"Wykres r(t) wykonany metodą \n Metoda Rungego-Kutty rzędu 4 \n dla E={E}, lambda^2={lamb}, r0={r_0}, phi0={phi_0}, u0={round(u_0,1)}")
plt.xlabel('t (s)')
plt.ylabel('r')
plt.savefig(f"C:/Users/pawko/OneDrive/Pulpit/python/knfk/r-g_E={E}l={lamb}r(t).png")
plt.show()
#plt.plot(T, U)
#plt.show()
plt.grid(True)
plt.plot(PHI, R)
plt.title(f"Wykres r(phi) wykonany metodą \n Metoda Rungego-Kutty rzędu 4 \n dla E={E}, lambda^2={lamb}, r0={r_0}, phi0={phi_0}, u0={round(u_0,1)}")
plt.xlabel('phi')
plt.ylabel('r')
plt.savefig(f"C:/Users/pawko/OneDrive/Pulpit/python/knfk/r-g_E={E}l={lamb}r(p).png")
plt.show()
#plt.plot(R, PHI)
#plt.title(f"Wykres r(phi) wykonany metodą predictor corector \n dla E={E}, lambda^2={lamb}, r0={r_0}, phi0={phi_0}, u0={round(u_0,1)}")
#plt.xlabel('r')
#plt.ylabel('phi')
#plt.show()
plt.grid(True)
plt.plot(T, PHI)
plt.title(f"Wykres phi(t) wykonany metodą \n Metoda Rungego-Kutty rzędu 4 \n dla E={E}, lambda^2={lamb}, r0={r_0}, phi0={phi_0}, u0={round(u_0,1)}")
plt.xlabel('t (s)')
plt.ylabel('phi')
plt.savefig(f"C:/Users/pawko/OneDrive/Pulpit/python/knfk/r-g_E={E}l={lamb}p(t).png")
plt.show()
plt.scatter(0, 0, color = 'r')
plt.plot(X, Y)
plt.title(f"Zmiana położenia punktu materialnego \n wykonana metodą Metoda Rungego-Kutty rzędu 4  \n dla E={E}, lambda^2={lamb}, r0={r_0}, phi0={phi_0}, u0={round(u_0,1)}")
plt.xlabel('x')
plt.ylabel('y')
#plt.xlim(-1, 1)
#plt.ylim(-1, 1)
plt.savefig(f"C:/Users/pawko/OneDrive/Pulpit/python/knfk/r-g_E={E}l={lamb}xy.png")
plt.show()









