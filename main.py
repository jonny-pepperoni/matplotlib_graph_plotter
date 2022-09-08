import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 500)

# given equations
eq1 = 400-x
eq2 = 600-x*2

# system of euations solution
x_solve = [200]
y_solve = [200]


def draw_graf():
    plt.plot(x, eq1, '-b', label='x+y=400')
    plt.plot(x, eq2, '-r', label='2x+y=600')
    plt.scatter(x_solve, y_solve, label='Optimizer x=200, y=200')

    plt.legend(loc=0)
    plt.grid()
    plt.show()


if __name__ == "__main__":
    draw_graf()
