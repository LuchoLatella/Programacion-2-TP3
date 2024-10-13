class TesterPizzeria:
    def main(self):
        # Crear variedades de pizza
        muzza = PizzaVariedad("Muzzarella", 1000.0)
        napo = PizzaVariedad("Napolitana", 1200.0)

        # Crear pizzas
        pizza1 = Pizza(muzza)
        pizza2 = Pizza(napo)

        # Crear orden
        orden = Orden(1, [pizza1, pizza2])

        # Crear empleados
        maestro = MaestroPizzero("Pipo")
        mozo1 = Mozo("Juan")

        # Flujo de la pizzería
        maestro.tomarPedido(orden)
        maestro.cocinar()
        pizzasParaMozo = maestro.entregar(orden)
        mozo1.tomarPizzas(pizzasParaMozo)
        mozo1.servirPizzas()

        # Calcular total de la orden
        total = orden.calcularTotal()
        print(f"Total de la orden: {total} pesos")

if __name__ == '__main__':
    tester = TesterPizzeria()
    tester.main()
