import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

'F0 = size of force due to bumpy'
'w = freq of forcing'
'v = velocity'



"my'' + by'' + ky = Fo(cos((2pi*v/xgap)t)"
"z = y' == mz' + bz + ky =  Fo(cos((2pi*v/xgap)t)" \
"this represents a 2nd order diffrential as a first order one so that the odeint function can be used"

'constants:'
m = 1
b = 1
k = 1

def dU_dt(U, t):
    "variables:"
    xgap = 1.0
    Fo = 1.0
    v = 10.0

    "y=U[0] and z=U[1] this function returns [y', z']"
    return [b * U[1], (-k*U[0]) + (-m*U[1]) + (np.cos((((2*math.pi)*v)/xgap)*t) * Fo)]

U0 = [0, 0]
ts = np.linspace(0, 2, 200)
Us = odeint(dU_dt, U0, ts)
ys = Us[:, 0]


plt.xlabel("time")
plt.ylabel("y")
plt.title("Washboard road")
plt.plot(ts, ys)
plt.show()



