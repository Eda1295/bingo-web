# 🎰 Bingo Web

Proyecto de Bingo web hecho con Django, desarrollado por fases como
proyecto de portfolio.

## Estado actual

✅ **Fase 1 — Preparación**: proyecto Django + app `bingo` creados y
funcionando.

Próxima fase: **Fase 2 — Bolillero** (sorteo de números del 1 al 90).

## Cómo correrlo localmente

```bash
# 1. Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate      # En Windows: venv\Scripts\activate

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Migrar base de datos
python manage.py migrate

# 4. Levantar el servidor
python manage.py runserver
```

Luego abrí http://127.0.0.1:8000/ en el navegador.

## Estructura

```
bingo_web/      -> configuración del proyecto Django
bingo/          -> app principal (lógica del bingo)
manage.py
requirements.txt
```
