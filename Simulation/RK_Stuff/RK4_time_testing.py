import numpy as np
import matplotlib.pyplot as plt
import time


def func(t,y):
    return -y


def realf(t):
    return np.exp(-t)


time_steps = np.array((1e0, 1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7))
error = np.array(())
time_run = np.array(())
for i in time_steps:
    dt = i
    tk = 0
    yk = 1
    tend = 1.0
    times = np.array((0))
    realy = np.array((1))
    appy = np.array((1))
    t0 = time.perf_counter()
    while tk < tend:
        print(tk)
        k1 = dt * func(tk, yk)
        k2 = dt * func(tk + (dt/2), yk + (k1/2))
        k3 = dt * func(tk + (dt/2), yk + (k2/2))
        k4 = dt * func(tk + dt, yk + k3)
        yk = yk + (1/6) * (k1 + 2 * k2 + 2 * k3 + k4)
        tk = tk + dt

        #times = np.append(times, tk)
    realy = realf(tk)
    appy = yk

    time_run = np.append(time_run, time.perf_counter() - t0)
    error = np.append(error, np.abs(realy - appy))
    #for i in range(len(times)):
     #   print(times[i], realy[i] - appy[i])
    #plt.figure(1)
    #plt.plot(times, realy)
    #plt.plot(times, appy, '.')
    #plt.show()

print(error)

plt.figure(2)
plt.loglog()
plt.plot(time_steps, time_run, '.')
plt.xlabel('Time Step')
plt.ylabel('Run Time')
plt.title('RK4 exp(-x)')


plt.figure(3)
plt.loglog()
plt.plot(time_steps, error, '.')
plt.xlabel('Time Step')
plt.ylabel('Error')
plt.title('RK4 exp(-x)')
plt.show()

