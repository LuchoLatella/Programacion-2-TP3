class PizzaVariedad:
    def __init__(self, nomVar: str, pre: float):
        self.__nombreVariedad = nomVar
        self.__precio = pre

    def establecerNombreVariedad(self, nomVar: str):
        self.__nombreVariedad = nomVar

    def establecerPrecio(self, pre: float):
        if pre > 0:
            self.__precio = pre

    def obtenerNombreVariedad(self):
        return self.__nombreVariedad

    def obtenerPrecio(self):
        return self.__precio

