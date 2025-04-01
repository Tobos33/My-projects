import numpy as np

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
dphi = 0
x = r_0*np.cos(phi)
y = np.sin(phi)*r_0

for i in range(60000):
    #print(r, phi, u)

    T.append(t)
    U.append(u)
    R.append(r)
    PHI.append(phi)
    X.append(x)
    Y.append(y)

    t = (i)*dt
    phi += runge_kutta_phi(r, dt)
    u += runge_kutta_u( r, dt)
    r += runge_kutta_r( u, dt)

    y = r*np.sin(phi)
    x = r*np.cos(phi)

    if r <= 0.0:
        print(phi, u)
        break

