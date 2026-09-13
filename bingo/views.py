from django.shortcuts import render


def home(request):
    """Vista temporal de la Fase 1: solo confirma que el proyecto
    y la app 'bingo' estan correctamente conectados.
    En la Fase 2 aca vamos a mostrar el bolillero."""
    return render(request, "bingo/home.html")
