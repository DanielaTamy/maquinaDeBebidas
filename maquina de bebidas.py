#Matriz principal da máquina de bebidas
maquina_bebidas = [[1, "coca-cola", 3.75, 2],
                   [2, "pepsi", 3.67, 5],
                   [3, "monster", 9.96, 1],
                   [4, "café", 1.25, 100],
                   [5, "redbull", 13.99, 2]]

notas = [[100, 2],
         [50, 10],
         [20, 12],
         [10, 20],
         [5, 15],
         [2, 15]]
moedas = [[1, 15],
          [0.5, 20],
          [0.25, 20],
          [0.1, 40],
          [0.05, 50],
          [0.01, 50]]

#função de entrada: o usuário define a bebida de sua escolha
def entrada():
    print("BEM-VINDO(A)")
    print("Opções disponiíveis:")
    for i in range(len(maquina_bebidas)):
        print(maquina_bebidas[i][0], "-", maquina_bebidas[i][1])
    bebida = int(input("escolha o ID da bebida desejada: "))
    return bebida

#função que verifica se o id está válido e se há estoque disponível
def verificando_estoque(bebida):
    if bebida > len(maquina_bebidas):
        print("ID de bebida inválida")
        return 0
    else:
        bebida_escolhida = maquina_bebidas[bebida - 1]
        print("A bebida escolhida foi:", bebida_escolhida[1])
        estoque = bebida_escolhida[3]
        print("Verificando estoque...")
        if estoque > 0:
            print("Estoque disponível: ", estoque)
            return estoque
        else:
            print("Desculpe, a bebida que você escolheu não está disponível em nosso estoque")
        return 0

#a função de compra recebe o pagamento do usuário
def compra(bebida, estoque):
    if estoque > 0:
        preco = maquina_bebidas[bebida - 1][2]
        print("Valor da bebida: R$", preco)
        pagamento = float(input("Digite o valor inserido na máquina: R$ "))
        while pagamento < preco:
            print("Pagamento insuficiente, insira o pagamento novamente na máquina")
            pagamento = float(input("Digite o valor inserido na máquina: R$ "))
        return pagamento

#a função calcula o troco, possui um estoque
def calculo_troco(pagamento, bebida, notas, moedas):
    preco = maquina_bebidas[bebida - 1][2]
    troco = pagamento - preco
    print("Troco: R$", round(troco, 2))
    for nota in notas:
        valor_nota = nota[0]
        estoque_nota = nota[1]
        #a função min() garante que se limite a quantidade diponível do estoque
        quantidade = min(int(troco / valor_nota), estoque_nota)
        if quantidade > 0 and quantidade <= estoque_nota:
            troco -= quantidade * valor_nota #atualiza o valor do troco
            if troco > 0 and troco < 0.01:
                troco = 0.01
                quantidade += 1
            print(quantidade, "nota(s) de R$", valor_nota)
            nota[1] -= quantidade #atualiza o estoque de notas
        elif quantidade > estoque_nota:
            print("Desculpe, não há notas suficientes em estoque")
            return False
    for moeda in moedas:
        valor_moeda = moeda[0]
        estoque_moeda = moeda[1]
        quantidade = int(troco / moeda[0])
        if quantidade > 0 and quantidade <= estoque_moeda:
            troco -= quantidade * moeda[0]
            if troco > 0 and troco < 0.01:
                troco = 0.01
                quantidade += 1
            print(quantidade, "moeda(s) de R$", valor_moeda)
            moeda[1] -= quantidade
        elif quantidade > estoque_moeda:
            print("Desculpe, não há moedas suficientes em estoque")
            return False
    return True

#função dentro do modo administrador que permite o usuário escolher oq deseja
def modo_administrador():
    while True:
        print("MODO ADMINISTRADOR ATIVADO")
        print("Digite uma das opções disponíveis: \n"
              "1 - cadastrar novo produto \n"
              "2 - editar produto \n"
              "3 - remover produto \n"
              "4 - sair")
        adm = int(input("Digite a opção desejada:"))
        if adm == 1:
            cadastro()
        elif adm == 2:
            editar()
        elif adm == 3:
            remover()
        elif adm == 4:
            return False
        else:
            print("opção não disponível, tente novamente")

#função para cadastrar um novo produto
def cadastro():
    ID = len(maquina_bebidas) + 1
    nome = input("Digite o nome do novo produto:")
    preco = float(input("Digite o preço do novo produto:"))
    estoque = int(input("Digite a quantidade do novo produto:"))
    cadastro_produto = [ID, nome, preco, estoque]
    maquina_bebidas.append(cadastro_produto)
    print("Cadastro realizado com sucesso")

#função para editar os dados do produto
def editar():
    ID = int(input("Digite o ID do produto a ser editado: "))
    if ID < 1 or ID > len(maquina_bebidas):
        print("ID de produto inválido")
    else:
        produto = maquina_bebidas[ID - 1]
        print("Produto escolhido:", produto)
        nome = input("Digite o nome: ")
        preco = float(input("Digite o preço : "))
        estoque = int(input("Digite o estoque: "))
        produto[1] = nome
        produto[2] = preco
        produto[3] = estoque
        print(
            "Produto alterado com sucesso")

#função para remover algum produto
def remover():
    ID = int(input("Digite o ID do produto a ser removido: "))
    if ID < 1 or ID > len(maquina_bebidas):
        print("ID de produto inválido")
    else:
        produto = maquina_bebidas[ID - 1]
        print("Produto escolhido:", produto)
        maquina_bebidas.pop(ID - 1)
        print("Produto removido com sucesso!")
        for i in range(len(maquina_bebidas)):
            maquina_bebidas[i][0] = i + 1

#ordem de execução do código
while True:
    print("Escolha o modo da máquina de bebidas:")
    print("Modos disponíveis: 1 - administrador 2 - cliente")
    modo = int(input("Entre com o modo: "))
    if modo == 1:
        modo_administrador()
    else:
        bebida = entrada()
        estoque = verificando_estoque(bebida)
        pagamento = compra(bebida, estoque)
        if estoque != 0:
            troco = calculo_troco(pagamento, bebida, notas, moedas)
            if troco:
                print("Compra concluída com sucesso! Muito obrigada, volte sempre!")
                maquina_bebidas[bebida - 1][3] -= 1
            else:
                print("Compra cancelada devido à falta de notas ou moedas em estoque.")
    print("===================================================================== \n")

