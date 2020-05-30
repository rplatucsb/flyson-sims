import numpy as np
import matplotlib.pyplot as plt

'''
Program the does a 4th order Runge-Kutta integration
on n user defined functions, define the function using 
func1 and func2 as an example, and add the new function to 
the numpy array funcs. Also each function needs an initial y
value to start at, add that to the numpy array yk
'''

# functions to integrate
def func1(t, y):
    return 1 + y ** 2


def func2(t, y):
    return -y

# analytical solutions to equations above
# add any new equations to realfuncs array
def realf1(t):
    return np.tan(t)


def realf2(t):
    return np.exp(-t)

# time step, start time, and stop time
dt = 0.001
tk = 0
tend = 10.0

# arrays tht have the store the current (initial in the first step) y values,
# the diff eq's, the analytical solutions, and the times calculations were performed
yk = np.array([1], dtype='float64')
funcs = np.array([func2], dtype='object')
realfuncs = [realf2]
times = np.array((0))

# adding the initial y values to the array containing all the true points of the
# solution, uncomment if you want to calculate and graph
realy = np.zeros((len(realfuncs), int(tend / dt) + 1), dtype='float64')
for i in range(len(realfuncs)):
    realy[i][0] = yk[i]

# adding initial values tot he array containing all the calculates points
appy = np.zeros((len(funcs), int(tend / dt) + 1), dtype='float64')
for i in range(len(funcs)):
    appy[i][0] = yk[i]

# loop that does the Runge-Kutta calculations and adds the results to the appropriate arrays
while round(tk / dt) < round(tend / dt):
    tk += dt
    times = np.append(times, tk)
    for i in range(len(funcs)):
        k1 = dt * funcs[i](tk, yk[i])
        k2 = dt * funcs[i](tk + (dt / 2), yk[i] + (k1 / 2))
        k3 = dt * funcs[i](tk + (dt / 2), yk[i] + (k2 / 2))
        k4 = dt * funcs[i](tk + dt, yk[i] + k3)
        yk[i] += (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        appy[i][round(tk / dt)] = yk[i]
        # realy[i][round(tk / dt)] = realfuncs[i](tk)  Uncomment if you want to calculate the actual solutions

# prints out the final y values
print(yk)

# plots all the functions we solved for
plt.figure(1)
for i in range(len(funcs)):
    plt.plot(times, appy[i], '.')
    # plt.plot(times, realy[i])  If your diff eq is analytically solvable, uncomment and define the real function with
                                 # the diff eq
plt.show()
