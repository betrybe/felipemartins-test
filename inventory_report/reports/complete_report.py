from inventory_report.reports.simple_report import SimpleReport


class CompleteReport():

    def generate(lista_de_dicts):

        # A classe CompleteReport herda o método generate de SimpleReport.

        simple_result = SimpleReport.generate(lista_de_dicts=lista_de_dicts)

        # Lista de nomes das empresas através da lista de dicionários.

        nome_da_empresa = []

        for x in lista_de_dicts:
            nome_da_empresa.append(x['nome_da_empresa'])

        # Bloco que monta o relatório completo com informações
        # sobre as empresas e quantidades de produtos estocados.

        frase = "Produtos estocados por empresa: \n"
        lix = []

        for x in range(0, len(nome_da_empresa)):
            if nome_da_empresa[x] in lix:
                pass
            else:
                nome = nome_da_empresa[x]
                quantidade = nome_da_empresa.count(nome)
                lix.append(nome)
                frase += "- " + nome + ": "
                frase += str(quantidade) + "\n"

        # Une-se o resultado simples com o obtido do bloco anterior.

        completo = simple_result + "\n" + frase

        return(completo)
