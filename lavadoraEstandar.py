from lavadora import Lavadora
import pygame
from time import sleep

class LavadoraEstandar(Lavadora):

    def __init__(self, kilos: float, estrato: int, tiempo_lavado: int, potencia_kw: float, tipo_ropa: int):
        super().__init__(kilos, estrato, tiempo_lavado, potencia_kw, tipo_ropa)

    def encender(self):
        self.estado = True
        print("Lavadora estándar encendida.")
        pygame.mixer.init()
        pygame.mixer.music.load("../Lavanderia/sonidos/c-371145.mp3")
        pygame.mixer.music.play()
        sleep(3)
    
    def _validar_kilos(self):
        return super()._validar_kilos()

    def _llenar(self):
        return super()._llenar()

    def _lavar(self):
        return super()._lavar() + " utilizando lavadora estándar."
    
    def _enjuagar(self):
        return super()._enjuagar()
    
    def _secar(self):
        return super()._secar()
    
    def ciclo_terminado(self):
        return super().ciclo_terminado()

    def mostrar_informacion(self):
        return super().mostrar_informacion() + "Tipo de lavadora: Estándar."
