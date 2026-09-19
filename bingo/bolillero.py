import random


class Bolillero:
    """Lógica del bolillero de bingo: números del 1 al 90,
    sorteo aleatorio sin repetir, con historial.

    Esta clase no sabe nada de Django, sesiones ni base de datos:
    solo maneja la lógica pura, para que sea fácil de testear.
    """

    TOTAL_NUMEROS = 90

    def __init__(self, disponibles=None, historial=None):
        if disponibles is None:
            self.disponibles = list(range(1, self.TOTAL_NUMEROS + 1))
        else:
            self.disponibles = list(disponibles)

        self.historial = list(historial) if historial else []

    def sortear(self):
        """Saca un número al azar de los disponibles, lo mueve
        al historial y lo devuelve. Si ya no quedan números,
        devuelve None (partida terminada)."""
        if not self.disponibles:
            return None

        numero = random.choice(self.disponibles)
        self.disponibles.remove(numero)
        self.historial.append(numero)
        return numero

    @property                               #convierte un método en algo que se lee como un atributo
    def ultimo_numero(self):
        return self.historial[-1] if self.historial else None

    @property
    def terminado(self):
        return len(self.disponibles) == 0
    