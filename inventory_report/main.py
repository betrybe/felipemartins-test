import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    # Captura de exceção, caso aconteça

    if len(sys.argv) < 3:
        return sys.stderr.write("Verifique os argumentos\n")

    # Estabelecendo os parâmetros usando "sys.argv" e preparando
    # o "split" para identificação da extensão

    path = sys.argv[1]
    tipo = sys.argv[2]
    split = str(path).split(sep="/")
    report = None

    # Identificação da extensão do arquivo.

    if ".csv" in split[-1]:
        report = InventoryRefactor(CsvImporter)
    elif ".json" in split[-1]:
        report = InventoryRefactor(JsonImporter)
    elif ".xml" in split[-1]:
        report = InventoryRefactor(XmlImporter)

    # Escrita do arquivo

    sys.stdout.write(report.import_data(path, tipo))
