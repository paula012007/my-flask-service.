# my-flask-service.


1. Estructura del proyecto Flask

Aquí tienes una estructura recomendada para el código base:

mi_servicio/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── models.py
├── tests/
│   └── test_routes.py
├── requirements.txt
├── .gitignore
├── README.md
├── .github/
│   └── workflows/
│       └── ci-cd.yml
└── run.py


---

2. Código base

app/__init__.py

from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import main
    app.register_blueprint(main)

    return app

app/routes.py

from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "Hola desde Flask"

run.py

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)


---

3. Archivo requerido

Flask==2.2.5
pytest==7.4.0


---

4. Pipeline CI/CD

.github/workflows/ci-cd.yml

name: CI/CD

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run tests
        run: |
          pytest


---

5. README

# Mi Servicio Flask

## Requisitos
- Python 3.10+
- pip

## Configuración del entorno
```bash
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows
pip install -r requirements.txt

Ejecutar el servicio

python run.py

Ejecutar tests

pytest

CI/CD


