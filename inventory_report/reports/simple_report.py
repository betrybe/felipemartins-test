from datetime import datetime


class SimpleReport():

    @classmethod
    def generate(self, lista_de_dicts):

        # São criadas algumas listas a partir do dicionário,
        # as listas de datas são ordenadas para se obter os dados
        # que queremos.

        nome_do_produto = []
        nome_da_empresa = []
        fab = []
        val = []

        for x in lista_de_dicts:
            nome_do_produto.append(x['nome_do_produto'])
            nome_da_empresa.append(x['nome_da_empresa'])
            fab.append(datetime.strptime(x['data_de_fabricacao'], '%Y-%m-%d'))
            val.append(datetime.strptime(x['data_de_validade'], '%Y-%m-%d'))

        fab.sort()
        val.sort()
        xx = 0
        maior = 0
        nome_maior = ''

        # Aqui obtém-se a data a empresa que possui mais produtos e também
        # a data mais próxima do momento da obtenção do relatório.

        for x in range(0, len(val)):
            nome = nome_da_empresa[x]
            quantidade = nome_da_empresa.count(nome_da_empresa[x])
            if quantidade > maior:
                maior = quantidade
                nome_maior = nome
            if val[xx] < datetime.today():
                xx += 1

        dat_fab_mais_antiga = fab[0].strftime('%Y-%m-%d')
        dat_val_mais_proxima = val[xx].strftime('%Y-%m-%d')

        return('Data de fabricação mais antiga: ' + dat_fab_mais_antiga + '\n'
               'Data de validade mais próxima: ' + dat_val_mais_proxima + '\n'
               'Empresa com maior quantidade de produtos estocados: ' +
               nome_maior + '\n')
