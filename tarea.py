class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print_info(self):
        print("     Customer:", self.get_customer())
        print("     Quantity:", self.get_qty())
        print("     ------------")

    def get_qty(self):
        return self.qtty

    def get_customer(self):
        return self.customer


class QueueInterface:
    def size(self):
        pass

    def is_empty(self):
        pass

    def front(self):
        pass

    def enqueue(self, info):
        pass

    def dequeue(self):
        pass


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Definir el primer nodo (top)
top = Node(Order(10, "Example Customer"))  # Ejemplo de creación de un nodo con un pedido

# Implementación del bucle while
node = top
while node is not None:
    # Imprime aquí la información del nodo
    node.data.print_info()
    node = node.next
