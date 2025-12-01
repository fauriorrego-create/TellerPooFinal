from time import sleep
from abc import ABC, abstractmethod
import pygame

class Lavadora(ABC):
    precio_kilo = 10000
    aumento_especial = 0.05   # 5%
    iva = 0.19

    def __init__(self, kilos: float, estrato: int, tiempo_lavado: int, potencia_kw: float, tipo_ropa: int):
        self._kilos = kilos
        self._estrato = estrato
        self._tiempo_lavado = tiempo_lavado
        self._potencia_kw = potencia_kw
        self._tipo_ropa = tipo_ropa

    # Getters
    def get_kilos(self):
        return self._kilos    
    
    def get_tipo_ropa(self):
        return self._tipo_ropa
    
    def get_tiempo_lavado(self):
        return self._tiempo_lavado
    
    def get_potencia_kw(self):
        return self._potencia_kw
    
    def get_estrato(self):
        return self._estrato

    # Métodos abstractos
    @abstractmethod
    def encender(self):
        pass

    # PROCESOS DE LAVADO
    def _validar_kilos(self):
        print("Validando kilos de ropa...")
        pygame.mixer.init()
        pygame.mixer.music.load("../Lavanderia/sonidos/notification-sound-effect-372475.mp3")
        pygame.mixer.music.play()
        sleep(2)
        return f"Kilos validados: {self._kilos} kg."

    def _llenar(self):
        print("Llenando la lavadora...")
        pygame.mixer.music.load("../Lavanderia/sonidos/agua-de-lavadora-27228.mp3")
        pygame.mixer.music.play()
        sleep(3)
        return "Lavadora llena."

    def _lavar(self):    
        print("Lavando...")
        pygame.mixer.music.load("../Lavanderia/sonidos/washingmachine-23215.mp3")
        pygame.mixer.music.play()
        sleep(3)
        return "Lavado completo."

    def _enjuagar(self):
        print("Enjuagando...")
        pygame.mixer.music.load("../Lavanderia/sonidos/notification-sound-effect-372475.mp3")
        pygame.mixer.music.play()
        sleep(3)
        return "Enjuague completo."

    def _secar(self):
        print("Secando...")
        pygame.mixer.music.load("../Lavanderia/sonidos/blow-dryer-low-setting-406740.mp3")
        pygame.mixer.music.play()
        sleep(3)
        return "Secado completo."

    def ciclo_terminado(self):
        return "Ciclo terminado."

    # COSTOS
    def calcular_costo(self) -> float:
        costo = self._kilos * self.precio_kilo

        # si la ropa es delicada
        if self._tipo_ropa in (1, 2, 3):
            costo += costo * self.aumento_especial

        costo_total = costo + (costo * self.iva)
        return costo_total

    def costo_energia(self) -> float:
        horas = self._tiempo_lavado / 60
        consumo = self._potencia_kw * horas

        tarifas = {2: 867.8, 3: 737.6, 4: 867.8, 5: 1014}

        return consumo * tarifas.get(self._estrato, 800)

    def mostrar_informacion(self):
        return (
            f"Kilos: {self._kilos}\n"
            f"Tipo de ropa: {self._tipo_ropa}\n"
            f"Tiempo lavado: {self._tiempo_lavado} min\n"
            f"Potencia: {self._potencia_kw} kW\n"
            f"Estrato: {self._estrato}\n"
        )

    # NUEVO MÉTODO PARA GANANCIA
    def unidad_empresario(self) -> float:
        """
        Calcula la ganancia neta para el empresario:
        Ganancia = costo total - costo energía
        """
        return self.calcular_costo() - self.costo_energia()
