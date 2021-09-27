import csv
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
import json
import xml.etree.cElementTree as et
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory():
    def import_data(path, tipo):

        # Bloco em que identifica a extensão do arquivo
        # e o transforma em uma lista de dicionários. Aqui
        # A complexidade do método poderia ser diminuída através
        # da utilização dos métodos criados nas classes imports
        # como não foi solicitado isso, não foi feita a alteração

        split = str(path).split(sep="/")

        if ".csv" in split[-1]:
             lista = CsvImporter.import_data(path)
        elif ".json" in split[-1]:
             lista = JsonImporter.import_data(path)
        elif ".xml" in split[-1]:
             lista = XmlImporter.import_data(path)

        # if ".csv" in split[-1]:
        #     lista = []
        #     with open(path, mode='r') as infile:
        #         reader = csv.DictReader(infile)
        #         for row in reader:
        #             lista.append(row)

        # elif ".json" in split[-1]:
        #     with open(path, mode='r') as infile:
        #         lista = json.load(infile)

        # elif ".xml" in split[-1]:
        #     lista = []
        #     dicio = {}
        #     tree = et.parse(path)
        #     root = tree.getroot()
        #     for elem in root:
        #         for subelem in elem:
        #             dicio[subelem.tag] = subelem.text
        #         lista.append(dicio)
        #         dicio = {}

        # Bloco que identifica que tipo de relatório queremos
        # e chama a respectiva classe e método.

        if tipo == "simples":

            simple = SimpleReport.generate(lista_de_dicts=lista)
            return(simple)

        elif tipo == "completo":

            complete = CompleteReport.generate(lista_de_dicts=lista)
            return(complete)
