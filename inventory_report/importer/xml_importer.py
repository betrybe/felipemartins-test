from inventory_report.importer.importer import Importer
import xml.etree.cElementTree as et

# Classe que herda o método da classe abstrata Importer no
# método abaixo é verificado se o arquivo tem a devida extensão
# e caso contrário é lançada uma exceção. Além disso, também é
# lido o arquivo e retornada uma lista de dicionários.


class XmlImporter(Importer):

    def import_data(path):
        split = str(path).split(sep="/")

        if ".xml" in split[-1]:
            lista = []
            dicio = {}
            tree = et.parse(path)
            root = tree.getroot()
            for elem in root:
                for subelem in elem:
                    dicio[subelem.tag] = subelem.text
                lista.append(dicio)
                dicio = {}

            return lista
        else:
            raise ValueError("Arquivo inválido")
