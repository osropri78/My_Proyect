"""Semana 1 — Python básico aplicado a datos.

Ejecuta:  python semana_01/python_basico.py
"""

from datos import VENTAS


# ---------------------------------------------------------------------------
# 1. Ejemplos resueltos (léelos y ejecútalos)
# ---------------------------------------------------------------------------

# Una lista se recorre con un bucle `for`.
print("Productos vendidos:")
for venta in VENTAS:
    # Para leer una columna del diccionario se usa venta["nombre_columna"].
    print(f"  - {venta['producto']} ({venta['categoria']})")

# Filtrar: quedarse solo con las filas que cumplen una condición.
# Esto es una "list comprehension": [expresión for x in lista if condición]
baratos = [v["producto"] for v in VENTAS if v["precio"] < 20]
print("\nProductos de menos de 20:", baratos)


# ---------------------------------------------------------------------------
# 2. TU TURNO
# ---------------------------------------------------------------------------

def total_ingresos(ventas):
    """Devuelve la suma de cantidad * precio de todas las ventas.

    TODO(tú): escribe aquí entre 3 y 5 líneas.
    Pista: crea una variable acumuladora que empiece en 0, recorre `ventas`
    con un for, y en cada vuelta súmale venta["cantidad"] * venta["precio"].
    """
    pass  # borra esta línea cuando escribas tu código


# ---------------------------------------------------------------------------
# 3. Comprobación automática (no hace falta tocarla)
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    resultado = total_ingresos(VENTAS)
    esperado = 3324.97
    if resultado is None:
        print("\n⏳ Aún no has escrito total_ingresos().")
    elif round(resultado, 2) == esperado:
        print(f"\n✅ ¡Correcto! Ingresos totales: {resultado:.2f}")
    else:
        print(f"\n❌ Obtuviste {resultado}, se esperaba {esperado}. ¡Revisa la fórmula!")
