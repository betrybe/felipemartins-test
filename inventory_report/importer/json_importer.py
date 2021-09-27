from inventory_report.importer.importer import Importer
import json

# Classe que herda o método da classe abstrata Importer no
# método abaixo é verificado se o arquivo tem a devida extensão
# e caso contrário é lançada uma exceção. Além disso, também é
# lido o arquivo e retornada uma lista de dicionários.


class JsonImporter(Importer):

    def import_data(path):
        split = str(path).split(sep="/")

        if ".json" in split[-1]:
            with open(path, mode='r') as infile:
                lista = json.load(infile)
            return lista
        else:
            raise ValueError("Arquivo inválido")
