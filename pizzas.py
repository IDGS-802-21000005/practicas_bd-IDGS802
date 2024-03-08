class PizzaManager:
    def __init__(self):
        self.pizzas = []
        self.next_id = 1

    def agregar_pizza(self, ingredientes, tamaño, num):
        
        subtotal = 0
        # Asignar precios base según el tamaño
        if tamaño == 'Grande':
            subtotal += 120
        elif tamaño == 'Mediana':
            subtotal += 80
        elif tamaño == 'Chica':
            subtotal += 40

        # Asignar precios adicionales según los ingredientes
        ingredientes_list = ingredientes.split(',')
        for ingrediente in ingredientes_list:
            if ingrediente == 'Champiñones':
                subtotal += 10
            if ingrediente == 'Jamón':
                subtotal += 10
            if ingrediente == 'Piña':
                subtotal += 10
        
        subtotal *= num
        
        
        pizza = {
            'id': self.next_id,
            'tamano': tamaño,
            'ingredientes':ingredientes,
            "num_pizzas": num,
            'subtotal': subtotal
        }
        
        self.pizzas.append(pizza)
        self.next_id += 1

    def eliminar_pizza(self, id):
        for pizza in self.pizzas:
            if pizza['id'] == id:
                self.pizzas.remove(pizza)
                return True
        return False
    
    def eliminar_pizzas(self):
        self.pizzas = []
        return True

    def obtener_pizzas(self):
        return self.pizzas
    
    def obtener_cliente(self):
        return self.client
    
    def total(self):
        total = 0
        for pizza in self.pizzas:
            total += pizza['subtotal']
        return total

# Ejemplo de uso
# pizza_manager = PizzaManager()
# pizza_manager.agregar_pizza('Champiñon,Jamon,Piña', 'Grande',1)
# pizza_manager.agregar_pizza('Champiñon,Piña', 'Mediana', 3)
# print(pizza_manager.obtener_pizzas())

# Eliminar una pizza por ID
# pizza_manager.eliminar_pizza(1)
# print(pizza_manager.obtener_pizzas())