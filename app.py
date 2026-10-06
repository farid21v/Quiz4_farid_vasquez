"""Generador de Números Aleatorios - aplicación web con Flask."""
import random

from flask import Flask, render_template, request

app = Flask(__name__)

MAX_CANTIDAD = 1000  # límite para evitar páginas gigantes


def validar(minimo, maximo, cantidad):
    """Convierte los textos a enteros y valida las reglas.
    Devuelve (min, max, cantidad, error). Si hay error, los números son None."""
    try:
        minimo = int(minimo)
        maximo = int(maximo)
        cantidad = int(cantidad)
    except (TypeError, ValueError):
        return None, None, None, "Todos los campos deben ser números enteros válidos."

    if minimo >= maximo:
        return None, None, None, "El número mínimo debe ser menor que el máximo."
    if cantidad <= 0:
        return None, None, None, "La cantidad de números debe ser mayor que 0."
    if cantidad > MAX_CANTIDAD:
        return None, None, None, f"La cantidad máxima permitida es {MAX_CANTIDAD}."
    return minimo, maximo, cantidad, None


@app.route("/", methods=["GET", "POST"])
def index():
    numeros = None
    error = None
    # Valores por defecto (y para conservar lo que escribió el usuario)
    datos = {"minimo": "1", "maximo": "100", "cantidad": "5"}

    if request.method == "POST":
        datos = {
            "minimo": request.form.get("minimo", "").strip(),
            "maximo": request.form.get("maximo", "").strip(),
            "cantidad": request.form.get("cantidad", "").strip(),
        }
        minimo, maximo, cantidad, error = validar(**datos)
        if error is None:
            numeros = [random.randint(minimo, maximo) for _ in range(cantidad)]

    return render_template("index.html", numeros=numeros, error=error, datos=datos)


if __name__ == "__main__":
    app.run(debug=True)
