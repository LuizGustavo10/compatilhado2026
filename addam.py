


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 200)
(line,) = ax.plot(x, np.sin(x))

ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.5, 1.5)
ax.set_title("Animação de Onda Senoidal")


def update(frame):
    line.set_ydata(np.sin(x + frame * 0.1))
    return (line,)


ani = FuncAnimation(fig, update, frames=100, interval=30, blit=True)
plt.show()