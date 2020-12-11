import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

'F0 = size of force due to bumpy'
'w = freq of forcing'
'v = velocity'



"mz'' + cz' + kz = 4kh + mg"

"this represents a 2nd order diffrential as a first order one so that the odeint function can be used"

"constants:"
mL = 386007
mU = 159207
b = 1
k = 1


def dU_dt(U, t = 1):
    "variables:"
    print("t", t)
    mg = 9.8 * mL
    h = 0.99
    c =1
    "h = np.sin(0.0034/int(t))"


    "y = z'"
    "z=U[0] and y=U[1] this function returns [z', y']"
    return [c * U[1], - (-4*k*U[0]) - (-mL*U[1]) + (4*k*np.sin(2)) + mg]

U0 = [0, 0]
ts = np.linspace(1, 2, 200)
Us = odeint(dU_dt, U0, ts)
ys = Us[:, 0]


plt.xlabel("time")
plt.ylabel("y")
plt.title("Washboard road")
plt.plot(ts, ys)
plt.show()



