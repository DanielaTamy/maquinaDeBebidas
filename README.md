# 🥤 Máquina de Bebidas Automática
Junho/2023
Raciocínio Algorítmico - Ciência da computação 1° período PUCPR

Este projeto implementa uma máquina de bebidas automática em Python. A máquina permite que os usuários escolham uma bebida, façam o pagamento e recebam o troco. Além disso, inclui um modo administrador para gerenciar os produtos disponíveis.

## 📂 Estrutura do Projeto

- **maquina_bebidas**: Lista contendo o ID, nome, preço e estoque das bebidas disponíveis.
- **notas**: Lista contendo as denominações e a quantidade de notas disponíveis para troco.
- **moedas**: Lista contendo as denominações e a quantidade de moedas disponíveis para troco.

## 🚀 Funcionalidades

### Modo Cliente

1. **Entrada de Bebida**: O usuário escolhe uma bebida com base no ID.
2. **Verificação de Estoque**: O programa verifica se a bebida escolhida está disponível.
3. **Pagamento**: O usuário insere o valor do pagamento. Se o valor inserido for insuficiente, será solicitado mais dinheiro.
4. **Cálculo de Troco**: A máquina calcula o troco e devolve em notas e moedas, de acordo com o estoque disponível.
5. **Confirmação de Compra**: Se o troco puder ser fornecido, a compra é concluída e o estoque da bebida é atualizado.

### Modo Administrador

1. **Cadastro de Produtos**: O administrador pode adicionar novos produtos à máquina.
2. **Edição de Produtos**: Permite alterar o nome, preço e quantidade em estoque de qualquer produto.
3. **Remoção de Produtos**: O administrador pode remover produtos da lista.
4. **Sair**: Opção para sair do modo administrador.

## 🎮 Como Usar

1. **Executando o Modo Cliente**:
   - O usuário escolhe o modo **Cliente**.
   - O programa exibirá as bebidas disponíveis e solicitará que o usuário selecione o ID da bebida desejada.
   - Após escolher a bebida, o usuário insere o valor do pagamento.
   - O troco será calculado e exibido, e a compra será confirmada se houver troco suficiente em estoque.

2. **Executando o Modo Administrador**:
   - O administrador escolhe o modo **Administrador**.
   - O administrador pode adicionar, editar ou remover produtos da máquina.


## 🛠️ Como Executar

1. Baixe ou clone este repositório.
2. Execute o arquivo Python com o comando:
   ```bash
   python maquina_bebidas.py
