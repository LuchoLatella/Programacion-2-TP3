from orden import Orden
from pizza import Pizza

class MaestroPizzero:
    def __init__(self, nom: str):
        self.__nombre = nom
        self.__ordenes = []

    def establecerNombre(self, nom: str):
        self.__nombre = nom

    def tomarPedido(self, orden: Orden):
        if orden.obtenerEstadoOrden() == Orden.ESTADO_INICIAL:
            self.__ordenes.append(orden)

    def cocinar(self):
        for orden in self.__ordenes:
            if orden.obtenerEstadoOrden() == Orden.ESTADO_INICIAL:
                print(f"{self.__nombre}: cocinando las pizzas de la orden {orden.obtenerNroOrden()}")
                orden.establecerEstadoOrden(Orden.ESTADO_PARA_ENTREGAR)
                for pizza in orden.obtenerPizzas():
                    pizza.establecerEstado(Pizza.ESTADO_COCINADA)

    def entregar(self, orden: Orden):
        if orden.obtenerEstadoOrden() == Orden.ESTADO_PARA_ENTREGAR:
            pizzasAEntregar = []
            for pizza in orden.obtenerPizzas():
                if len(pizzasAEntregar) < 2:
                    pizza.establecerEstado(Pizza.ESTADO_ENTREGADA)
                    pizzasAEntregar.append(pizza)
            print(f"{self.__nombre}: Entregando {len(pizzasAEntregar)} pizzas")
            if all(pizza.obtenerEstado() == Pizza.ESTADO_ENTREGADA for pizza in orden.obtenerPizzas()):
                orden.establecerEstadoOrden(Orden.ESTADO_ENTREGADA)
        return pizzasAEntregar
