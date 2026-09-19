import numpy as np
import matplotlib.pyplot as plt

t0 = 0
tf = 1
y0 = 1
h = 0.2

def solucion_exacta(t):
    return np.exp(t)


t = np.arange(t0, tf + h, h)
y_euler = np.zeros(len(t))
y_euler[0] = y0


for n in range(len(t) - 1):
    # f(t,y) = y
    f = y_euler[n]

    # Fórmula de Euler:
    # y(n+1) = y(n) + h*f(t(n), y(n))
    y_euler[n + 1] = y_euler[n] + h * f


y_exacta = solucion_exacta(t)
print("Resultados:")
print("-" * 50)
print("   t       Euler          Exacta        Error")
print("-" * 50)

for i in range(len(t)):
    error = abs(y_exacta[i] - y_euler[i])

    print(f"{t[i]:5.1f}   {y_euler[i]:10.6f}   "
          f"{y_exacta[i]:10.6f}   {error:10.6f}")


# Valores más pequeños para que la solución exacta
# aparezca como una curva suave
t_suave = np.linspace(0, 1, 100)

plt.plot(
    t_suave,
    solucion_exacta(t_suave),
    label="Solución exacta",
    color="blue"
)

plt.plot(
    t,
    y_euler,
    "o--",
    label="Método de Euler",
    color="red"
)

plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Solución exacta vs. Método de Euler")
plt.grid(True)
plt.legend()

plt.show()

