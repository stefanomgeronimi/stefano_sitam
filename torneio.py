class Lutadores:

    def __init__(self, nome_lutador, idade, peso, forca, faixa, arte_marcial):

        self.nome_lutador = nome_lutador
        self.idade = idade
        self.peso = peso
        self.forca = forca
        self.faixa = faixa
        self.arte_marcial = arte_marcial

    def __str__(self):
        return f'''Lutador {self.nome_lutador}, {self.idade} anos, {self.peso}kg, força {self.forca}, 
        faixa {self.faixa} de {self.arte_marcial}'''


class Torneios:

    def __init__(self, nome_do_torneio, arte_marcial, faixa, menor_peso, maior_peso):
        self.nome_do_torneio = nome_do_torneio
        self.arte_marcial = arte_marcial
        self.faixa = faixa
        self.menor_peso = menor_peso
        self.maior_peso = maior_peso
        self.lutadores_torneio = []

    def __str__(self):
        return f'''
        Nome do Torneio: {self.nome_do_torneio}
        Arte Marcial: {self.arte_marcial}
        Faixa: {self.faixa}
        Peso Mínimo: {self.menor_peso}
        Peso Máximo: {self.maior_peso}'''

    def add_lutador(self, lutador):
        self.lutadores_torneio.append(lutador)

torneios = []
lutadores = []

def cadastrar_torneio(torneio):
    torneios.append(torneio)

def cadastrar_lutador(lutador):
    lutadores.append(lutador)

def inscrever_lutador(nome_lutador, idade, peso, forca, faixa, arte_marcial): #Criar função
    print('FUNÇÃO EM CRIAÇÃO')

def exibir_torneios():
    for torneio in torneios:
        print(torneio)

def exibir_lutadores():
    for lutador in lutadores:
        print(lutador)

def exibir_detalhes():
        print('FUNÇÃO EM CRIAÇÃO')

resposta_1 = 0
resposta_2 = 0
resposta_3 = 0

while resposta_1 or resposta_2 != 9:

    print('\nBem-vindo ao SITAM (Sistema Integrado de Torneios de Artes Marciais)!\n')
    print('''
    [  1  ] MENU DO TORNEIO
    [  2  ] MENU DE LUTADOR''')
    resposta_1 = int(input('Escolha uma alternativa: '))

    if resposta_1 == 1:
        print('''\nMENU DO TORNEIO\n
        [  1  ] Criar Torneio
        [  2  ] Inscrever Lutador
        [  3  ] Ver Torneios Existentes
        [  4  ] Ver Ranking de Torneio
        [  5  ] Ver Lutadores Inscritos em Torneio
        [  6  ] Realizar Luta
        PRESSIONE [  9  ] A QUALQUER MOMENTO PARA VOLTAR AO INÍCIO''')
        
        resposta_2 = int(input('Escolha uma alternativa: '))

        if resposta_2 == 1:
            nome_do_torneio = str(input('Nome do torneio: '))
            arte_marcial = str(input('Arte Marcial: '))
            faixa = str(input('Faixa:  '))
            menor_peso = int(input('Peso Mínimo: '))
            maior_peso = int(input('Peso Máximo: '))
            torneio = []
            torneio.append(Torneios(nome_do_torneio, arte_marcial, faixa, menor_peso, maior_peso))
            torneios.append(torneio)

        elif resposta_2 == 2: # Esse é o código para inscrição
            exibir_lutadores()
            input('Escolha um lutador: ')
            resposta_a = lutadores[resposta_a]
            input('Escolha um torneio: ')
            resposta_b = torneios[resposta_b]
            resposta_b.add_lutador(resposta_a)

        elif resposta_2 == 3:
            exibir_torneios()

        elif resposta_2 == 4:
            exibir_torneios()
            resposta = input('Escolha um torneio: ')
            torneios[resposta]

        elif resposta_2 == 5:
            exibir_torneios()
            resposta = input('Escolha um torneio: ')
            escolha = torneios[resposta]
            for lutador in escolha:
                print(lutador)

        elif resposta_2 == 6:
            exibir_torneios()
            resposta = input('Escolha um torneio: ')
            escolha = torneios[resposta]
            for lutador in escolha:
                print(lutadores)
            lutador_a = input('Escolha o primeiro lutador: ')
            lutador_b = input('Escolha o segundo lutador: ')
            if lutador_a.forca >= lutador_b.forca:
                print(f'Lutador {lutador_a.nome_lutador} venceu a luta')
            else:
                print(f'Lutador {lutador_b.nome_lutador} venceu a luta')

        elif resposta_2 == 9:
            print('Voltando ao início...\n')

        else:
            print('O valor inserido é inválido')

    elif resposta_1 == 2:
        print('''\nMENU DE LUTADOR\n
        [  1  ] Cadastrar Lutador
        [  2  ] Ver Lutadores
        [  3  ] Ver Detalhes de Lutador
        ''')
        resposta_2 = int(input('Escolha uma alternativa: '))

        if resposta_2 == 1:
            nome_lutador = str(input('Nome do lutador: '))
            idade = int(input('Idade: '))
            peso = int(input('Peso (kg): '))
            forca = int(input('Força (0-100): '))
            faixa = str(input('Faixa: '))
            arte_marcial = str(input('Arte marcial: '))
            lutador = []
            lutador.append(Lutadores(nome_lutador, idade, peso, forca, faixa, arte_marcial))
            cadastrar_lutador(lutador)
            print(f'{nome_lutador} foi cadastrado com sucesso')
        
        elif resposta_2 == 2:
            for lutador in lutadores:
                print(lutador)
        
        elif resposta_2 == 3:
            exibir_lutadores()
            input('Escolha um lutador: ')
            resposta = lutadores[resposta]
            for informacoes in resposta:
                print(informacoes)

        elif resposta_2 == 9:
            print('Voltando ao início...\n')

    else:
        print('O valor inserido é inválido')

print(lutadores)