from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.inventory.inventory_iterator import InventoryIterator

# Implementação da classe InventoryRefactor


class InventoryRefactor:
    def __init__(self, classe):
        self.importer = classe
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path, tipo):

        lista = self.importer.import_data(path)

        self.data += lista

        if tipo == "simples":
            return SimpleReport.generate(self.data)

        elif tipo == "completo":
            return CompleteReport.generate(self.data)
