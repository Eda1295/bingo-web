from django.test import TestCase
from .bolillero import Bolillero


class BolilleroTests(TestCase):

    def test_empieza_con_90_numeros_disponibles(self):
        b = Bolillero()
        self.assertEqual(len(b.disponibles), 90)
        self.assertEqual(b.historial, [])

    def test_numeros_van_del_1_al_90(self):
        b = Bolillero()
        self.assertEqual(min(b.disponibles), 1)
        self.assertEqual(max(b.disponibles), 90)

    def test_sortear_devuelve_un_numero_valido(self):
        b = Bolillero()
        numero = b.sortear()
        self.assertIsNotNone(numero)
        self.assertTrue(1 <= numero <= 90)

    def test_sortear_no_repite_numeros(self):
        b = Bolillero()
        sorteados = [b.sortear() for _ in range(90)]
        self.assertEqual(len(sorteados), len(set(sorteados)))
        self.assertEqual(sorted(sorteados), list(range(1, 91)))

    def test_ultimo_numero_se_actualiza(self):
        b = Bolillero()
        numero = b.sortear()
        self.assertEqual(b.ultimo_numero, numero)

    def test_terminado_cuando_no_quedan_numeros(self):
        b = Bolillero()
        self.assertFalse(b.terminado)
        for _ in range(90):
            b.sortear()
        self.assertTrue(b.terminado)

    def test_sortear_despues_de_terminado_devuelve_none(self):
        b = Bolillero()
        for _ in range(90):
            b.sortear()
        self.assertIsNone(b.sortear())
        