from django.shortcuts import render, redirect
from .bolillero import Bolillero

SESSION_KEY = "bolillero"


def _cargar_bolillero(request):
    """Reconstruye el Bolillero a partir de lo guardado en la sesion."""
    data = request.session.get(SESSION_KEY)
    if not data:
        return Bolillero()
    return Bolillero(disponibles=data["disponibles"], historial=data["historial"])


def _guardar_bolillero(request, bolillero):
    request.session[SESSION_KEY] = {
        "disponibles": bolillero.disponibles,
        "historial": bolillero.historial,
    }


def home(request):
    bolillero = _cargar_bolillero(request)
    context = {
        "ultimo_numero": bolillero.ultimo_numero,
        "historial": list(reversed(bolillero.historial)),
        "cantidad_sorteados": len(bolillero.historial),
        "terminado": bolillero.terminado,
    }
    return render(request, "bingo/home.html", context)


def sortear(request):
    if request.method == "POST":
        bolillero = _cargar_bolillero(request)
        bolillero.sortear()
        _guardar_bolillero(request, bolillero)
    return redirect("home")


def reiniciar(request):
    if request.method == "POST":
        request.session.pop(SESSION_KEY, None)
    return redirect("home")