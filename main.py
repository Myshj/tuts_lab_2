import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import math


def main_1():
    k = 2
    t = np.arange(0, 25, 0.01)
    x = [
        k * t_i for t_i in t
    ]

    # Выходной сигнал
    plt.plot(t, x, 'b', label='x')
    plt.plot(t, t, 'r', label='u')
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.show()

    # h(t)
    h = [
        k for t_i in t
    ]
    plt.plot(t, h)
    plt.xlabel('t')
    plt.ylabel('h(t)')
    plt.show()

    # phi(w)
    w = np.arange(0, 100, 0.01)
    phi = [
        0 for w_i in w
    ]
    plt.plot(w, phi)
    plt.xlabel('w')
    plt.ylabel('phi(w)')
    plt.show()


def solver_5(X, t):
    k = 5
    a = 0.5
    return [
        -X[0] / a + k
    ]


def main_5():
    t = np.arange(0, 25, 0.01)
    asol = integrate.odeint(solver_5, [1], t)
    print(asol)

    plt.plot(t, asol[:, 0], 'b', label="x")
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.show()

    # h(t)
    h = [
        5 * math.exp(-t_i / 0.5) for t_i in t
    ]
    plt.plot(t, h)
    plt.xlabel('t')
    plt.ylabel('h(t)')
    plt.show()

    # phi(w)
    w = np.arange(0, 100, 0.01)
    phi = [
        90 - math.atan(0.5 * w_i) for w_i in w
    ]

    plt.plot(w, phi)
    plt.xlabel('w')
    plt.ylabel('phi(w)')
    plt.show()


if __name__ == '__main__':
    main_1()
    #main_5()