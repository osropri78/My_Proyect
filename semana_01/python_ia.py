"""Semana 1 — Python para IA: construye una neurona artificial a mano.

Una neurona hace tres cosas:
  1. Multiplica cada entrada por su peso (cuánto "importa" esa entrada).
  2. Suma todo y añade un sesgo.            -> z = x1*w1 + x2*w2 + ... + b
  3. Pasa z por una función de activación   -> un número entre 0 y 1

El paso 1+2 se llama PRODUCTO PUNTO y es la operación más usada en toda la IA:
redes neuronales, ChatGPT, recomendadores... todo son millones de productos punto.

Ejecuta:  python semana_01/python_ia.py
"""

import math


# ---------------------------------------------------------------------------
# 1. Ejemplos resueltos
# ---------------------------------------------------------------------------

# En IA, una lista de números se llama VECTOR. Cada posición es una característica.
alumno = [6, 8]          # [horas de estudio, horas de sueño]
pesos  = [0.8, 0.5]      # cuánto influye cada característica en aprobar

# zip() recorre dos listas a la vez, emparejando sus elementos por posición.
for x, w in zip(alumno, pesos):
    print(f"entrada {x} x peso {w} = {x * w}")


def sigmoide(z):
    """Función de activación: convierte cualquier número en uno entre 0 y 1.

    z muy negativo -> casi 0  |  z = 0 -> 0.5  |  z muy positivo -> casi 1
    Por eso se interpreta como una probabilidad.
    """
    return 1 / (1 + math.exp(-z))


# ---------------------------------------------------------------------------
# 2. TU TURNO
# ---------------------------------------------------------------------------

def producto_punto(a, b):
    """Multiplica a y b posición a posición y suma los resultados.

    Ejemplo: producto_punto([1, 2, 3], [4, 5, 6]) = 1*4 + 2*5 + 3*6 = 32

    TODO(tú): 3-4 líneas. Pista: acumulador en 0 + `for x, w in zip(a, b):`
    """
    pass  # borra esta línea cuando escribas tu código


# Esta función ya está hecha: fíjate en que USA tu producto_punto.
def neurona(entradas, pesos, sesgo):
    z = producto_punto(entradas, pesos) + sesgo
    return sigmoide(z)


# ---------------------------------------------------------------------------
# 3. Comprobación automática
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print()
    resultado = producto_punto([1, 2, 3], [4, 5, 6])
    if resultado is None:
        print("⏳ Aún no has escrito producto_punto().")
    elif resultado != 32:
        print(f"❌ producto_punto([1,2,3],[4,5,6]) dio {resultado}, debería dar 32.")
    else:
        print("✅ ¡producto_punto funciona! Tu neurona ya puede predecir:\n")
        alumnos = {"Ana": [2, 5], "Luis": [4, 6], "Marta": [6, 8]}
        for nombre, datos in alumnos.items():
            p = neurona(datos, pesos=[0.8, 0.5], sesgo=-6)
            print(f"  {nombre:6} estudio={datos[0]}h sueño={datos[1]}h -> "
                  f"probabilidad de aprobar: {p:.0%}")
