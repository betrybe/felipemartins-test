from collections.abc import Iterator

# Implementação da classe InventoryIterator com
# interface do iterador (Iterator).


class InventoryIterator(Iterator):

    def __init__(self, lista):
        self.lista = lista
        self.iter = 0

    def __next__(self):
        try:
            it = self.lista[self.iter]
            self.iter += 1
        except IndexError:
            raise StopIteration

        return it
