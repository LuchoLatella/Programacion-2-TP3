from pizza import Pizza

class Mozo:
    def __init__(self, nom: str):
        self.__nombre = nom
        self.__pizzas = []

    def establecerNombre(self, nom: str):
        self.__nombre = nom

    def tomarPizzas(self, pizzas: list):
        if len(self.__pizzas) + len(pizzas) <= 2:
            for pizza in pizzas:
            # Obtener el nombre de la variedad de la pizza antes de concatenar
                print(f"{self.__nombre}: Tomando pizza de {pizza.obtenerVariedad().obtenerNombreVariedad()}")
                self.__pizzas.append(pizza)


    def servirPizzas(self):
        for pizza in self.__pizzas:
            print(f"{self.__nombre}: Sirviendo pizza de {pizza.obtenerVariedad().obtenerNombreVariedad()}")
        self.__pizzas = []

    def obtenerEstadoLibre(self):
        return len(self.__pizzas) < 2
