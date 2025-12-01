from lavadora import Lavadora
import pygame
from time import sleep  

class LavadoraInteligente(Lavadora):       
    
    def __init__(self, kilos: float, estrato: int, tiempo_lavado: int, potencia_kw: float, tipo_ropa: int, wifi=True, sensores=True):
        super().__init__(kilos, estrato, tiempo_lavado, potencia_kw, tipo_ropa)
        self._wifi = wifi
        self._sensores = sensores

    def encender(self):
        self.estado = True
        print("Lavadora inteligente encendida.")
        pygame.mixer.init()
        pygame.mixer.music.load("../Lavanderia/sonidos/item-pick-up-38258.mp3")
        pygame.mixer.music.play()
        sleep(3)

    def _validar_kilos(self):
        return super()._validar_kilos()
    
    def detectar_tipo_ropa(self):
        print("Detectando tipo de ropa automáticamente mediante sensores...")
        sleep(2)
        return f"Tipo de ropa detectado: {self._tipo_ropa}"

    def conectar_wifi(self):
        if self._wifi:
            print("Conectando a la red WiFi...")
            sleep(2)
            return "Lavadora conectada correctamente."
        else:
            return "Esta lavadora no posee módulo WiFi."

    def _llenar(self):
        return super()._llenar()

    def _lavar(self):
        return super()._lavar() + " utilizando lavadora inteligente con wifi y sensores equipados."

    def _enjuagar(self):
        return super()._enjuagar()

    def _secar(self):
        return super()._secar()

    def ciclo_terminado(self):
        return super().ciclo_terminado()
    
    def enviar_reporte(self):
        print("Enviando reporte del ciclo mediante conexión WiFi...")
        sleep(2)
        return "Reporte enviado correctamente."

    def mostrar_informacion(self):
        return super().mostrar_informacion() + "Tipo de lavadora: Inteligente.\n"
