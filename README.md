# Pre-entrega Automation Testing - SauceDemo

Proyecto de automatizacion QA realizado con Python, Pytest y Selenium WebDriver sobre el sitio demo https://www.saucedemo.com/.

## Objetivo

Automatizar flujos basicos de navegacion, login, validacion de catalogo e interaccion con carrito en SauceDemo.

## Tecnologias utilizadas

- Python 3.10+
- Selenium WebDriver
- webdriver-manager
- Pytest
- pytest-html
- Git y GitHub
- Google Chrome

## Estructura

```text
pre-entrega-final/
  tests/
    test_saucedemo.py
  utils/
    saucedemo_helpers.py
  reports/
  screenshots/
  requirements.txt
  README.md
```

## Instalacion

Desde esta carpeta:

```bash
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements.txt
```

Las versiones estan fijadas en `requirements.txt` para que la instalacion sea reproducible.

En clase tambien se menciono instalar Selenium y webdriver-manager con:

```bash
pip install selenium
pip install webdriver-manager
```

Este proyecto deja ambos paquetes dentro de `requirements.txt` para instalarlos juntos.

Si usas Linux o macOS, el comando puede ser:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Ejecucion de pruebas

Desde la carpeta que contiene `pre-entrega-final`:

```bash
pre-entrega-final\.venv\Scripts\python.exe -m pytest pre-entrega-final/tests/test_saucedemo.py -v --html=pre-entrega-final/reports/reporte.html --self-contained-html
```

Tambien se puede ejecutar desde adentro de `pre-entrega-final`:

```bash
python -m pytest tests/test_saucedemo.py -v --html=reports/reporte.html --self-contained-html
```

## Casos automatizados

- Login exitoso con usuario `standard_user`.
- Validacion de redireccion a `/inventory.html`.
- Validacion de titulo visible `Products` y marca `Swag Labs`.
- Validacion de productos visibles en el catalogo.
- Obtencion del nombre y precio del primer producto.
- Agregado del primer producto al carrito.
- Validacion del contador del carrito.
- Validacion del producto agregado dentro del carrito.

## Evidencias

- El reporte HTML se genera en `reports/reporte.html`.
- Si una prueba falla, se guarda una captura automatica en `screenshots/`.
- Como la ultima ejecucion fue exitosa, la carpeta `screenshots/` no contiene capturas de fallos.
- El resumen de ejecucion queda documentado en `reports/resultado_ejecucion.txt`.

## Resultado de la ultima ejecucion

```text
3 passed in 20.20s
```

## Repositorio

Nombre sugerido para GitHub segun la consigna:

```text
pre-entrega-automation-testing-nombre-apellido
```

Reemplazar `nombre-apellido` por tus datos antes de crear el repositorio.
