# Generador de Números Aleatorios

## Descripción

Aplicación web sencilla, hecha con Python y Flask, que genera números aleatorios enteros dentro de un rango definido por el usuario. Se creó como tarea universitaria para practicar desarrollo de aplicaciones, documentación y control de versiones con Git/GitHub.

## Funcionalidades

- Ingresar el número mínimo, el número máximo y la cantidad de números a generar.
- Botón **Generar números** que muestra el resultado en pantalla.
- Se puede volver a generar sin reiniciar la aplicación (los valores se conservan en el formulario).
- Validaciones con mensajes de error claros:
  - El mínimo debe ser menor que el máximo.
  - La cantidad debe ser mayor que 0 (máximo 1000).
  - Solo se aceptan números enteros válidos.
- Interfaz limpia, moderna y adaptable a móviles.

## Tecnologías utilizadas

- Python 3
- Flask (servidor web y plantillas Jinja2)
- HTML5 y CSS3

## Requisitos

- Python 3.8 o superior
- pip (incluido con Python)
- Git (para clonar el repositorio)

## Instalación de dependencias

```bash
git clone https://github.com/farid21v/generador-numeros.git
cd Quiz4_farid_vasquez

# (Recomendado) crear un entorno virtual
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate

pip install -r requirements.txt
```

## Ejecución local

```bash
python app.py
```

Luego abre en el navegador: <http://127.0.0.1:5000>

## Ejemplo de uso

1. Escribe **Mínimo = 1**, **Máximo = 50** y **Cantidad = 6**.
2. Pulsa **Generar números**.
3. Aparecerán 6 números entre 1 y 50, por ejemplo: `7 23 41 3 18 50`.
4. Pulsa el botón de nuevo para obtener otra serie.

Si escribes un mínimo mayor o igual que el máximo, verás el mensaje: *"El número mínimo debe ser menor que el máximo."*

## Estructura del proyecto

```
generador-numeros/
├── app.py              # Lógica de la aplicación y validaciones
├── requirements.txt    # Dependencias (Flask)
├── README.md           # Documentación
├── .gitignore          # Archivos que Git debe ignorar
├── templates/
│   └── index.html      # Página con el formulario y los resultados
└── static/
    └── style.css       # Estilos de la interfaz
```
