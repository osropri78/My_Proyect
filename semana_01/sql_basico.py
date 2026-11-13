"""Semana 1 — SQL básico con SQLite.

SQLite viene incluido en Python: no hay que instalar nada.
Ejecuta:  python semana_01/sql_basico.py
"""

import sqlite3

from datos import VENTAS

# Creamos una base de datos en memoria y cargamos la tabla `ventas`.
conexion = sqlite3.connect(":memory:")
conexion.execute(
    "CREATE TABLE ventas (producto TEXT, categoria TEXT, cantidad INTEGER, precio REAL)"
)
conexion.executemany(
    "INSERT INTO ventas VALUES (:producto, :categoria, :cantidad, :precio)", VENTAS
)


def consultar(sql):
    """Ejecuta una consulta SQL e imprime el resultado como una tabla sencilla."""
    cursor = conexion.execute(sql)
    columnas = [c[0] for c in cursor.description]
    filas = cursor.fetchall()
    print(" | ".join(columnas))
    for fila in filas:
        print(" | ".join(str(x) for x in fila))
    print()
    return filas


# ---------------------------------------------------------------------------
# 1. Ejemplos resueltos
# ---------------------------------------------------------------------------

print("SELECT: elegir columnas")
consultar("SELECT producto, categoria FROM ventas")

print("WHERE: filtrar filas (igual que el `if` de la list comprehension en Python)")
consultar("SELECT producto, precio FROM ventas WHERE precio < 20")

print("ORDER BY: ordenar")
consultar("SELECT producto, precio FROM ventas ORDER BY precio DESC")


# ---------------------------------------------------------------------------
# 2. TU TURNO
# ---------------------------------------------------------------------------
# Escribe una consulta que devuelva, POR CADA categoría, sus ingresos totales
# (suma de cantidad * precio). Debe devolver dos columnas: categoria e ingresos.
#
# Pistas:
#   - SUM(...) suma los valores de una columna o de una expresión.
#   - GROUP BY categoria agrupa las filas que tienen la misma categoría.
#   - Puedes renombrar una columna con AS:  SUM(...) AS ingresos
#
# TODO(tú): escribe la consulta entre las comillas.
MI_CONSULTA = """

"""


# ---------------------------------------------------------------------------
# 3. Comprobación automática
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    if not MI_CONSULTA.strip():
        print("⏳ Aún no has escrito MI_CONSULTA.")
    else:
        print("Tu consulta:")
        filas = consultar(MI_CONSULTA)
        esperado = {"Electrónica": 2454.97, "Muebles": 780.0, "Papelería": 90.0}
        obtenido = {cat: round(total, 2) for cat, total in filas}
        if obtenido == esperado:
            print("✅ ¡Correcto! Acabas de hacer tu primer GROUP BY.")
        else:
            print(f"❌ Se esperaba {esperado}. ¡Revisa la consulta!")
