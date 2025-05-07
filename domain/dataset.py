from abc import ABC, abstractmethod


class Dataset(ABC):
    def __init__(self, fuente):
        self.__fuente = fuente
        self.__datos = None

    @property
    def datos(self):
        return self.__datos

    @datos.setter
    def datos(self, value):
        # validaciones
        self.__datos = value

    @abstractmethod
    def cargar_datos(self):
        pass

    def validar_datos(self):
        pass

    def transformar_datos(self):
        pass

    def mostrar_resumen(self):
        pass