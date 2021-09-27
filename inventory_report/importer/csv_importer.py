from inventory_report.importer.importer import Importer
import csv

# Classe que herda o método da classe abstrata Importer no
# método abaixo é verificado se o arquivo tem a devida extensão
# e caso contrário é lançada uma exceção. Além disso, também é
# lido o arquivo e retornada uma lista de dicionários.


class CsvImporter(Importer):

    def import_data(path):

        split = str(path).split(sep="/")

        if ".csv" in split[-1]:
            lista = []
            with open(path, mode='r') as infile:
                reader = csv.DictReader(infile)
                for row in reader:
                    lista.append(row)
            return lista
        else:
            raise ValueError("Arquivo inválido")
