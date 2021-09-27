from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory():
    def import_data(path, tipo):

        split = str(path).split(sep="/")

        if ".csv" in split[-1]:
          lista = CsvImporter.import_data(path)
        elif ".json" in split[-1]:
          lista = JsonImporter.import_data(path)
        elif ".xml" in split[-1]:
          lista = XmlImporter.import_data(path)

        if tipo == "simples":
          simple = SimpleReport.generate(lista_de_dicts=lista)
          return(simple)
        else:
          complete = CompleteReport.generate(lista_de_dicts=lista)
          return(complete)
