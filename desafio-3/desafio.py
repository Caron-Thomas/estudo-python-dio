import re

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[n] Cadastrar Novo Usuário 

=> """

usuarios = {}
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def saque(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:    R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def imprimir_extrato(saldo,/,*,extrato):
    print("\n=================== EXTRATO ===================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("================================================")

def criar_novo_usuario():
    global usuarios
    endereco = "Endereço não informado"
    cpf = re.sub(r'\D', '', input("Digite o CPF do novo usuário: \n"))
    if usuarios.get(cpf) is not None:
        print("Usuário já foi cadastrado no sistema")
        return
    
    nome = input('Digite o nome completo: \n')
    data_nascimento = input("Digite a data de nascimento no formato dd/MM/aa :\n")

    if(input("Cadastrar endereço: (S ou N): \n").lower() == "s"):
        endereco = cadastrar_endereco()

    usuarios[cpf] = {"nome":nome, "data de nascimento": data_nascimento, "endereço": endereco }
    usuario = usuarios.get(cpf)
    print(f'Usuário cadastrado com sucesso: \n {usuario}')
    

    
def cadastrar_endereco():
    logradouro = input("Digite o logradouro: \n")
    nro = ", " + input("Digite o número do imóvel: \n") 
    bairro = " - " +  input("Digite o bairro: \n") 
    cidade = input("Digite a cidade: \n")
    estado = "/" + input("Digite a sigla do estado: \n").upper()

    return logradouro + nro + bairro + " " + cidade + estado

    
while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        retorno = deposito(saldo = saldo, valor = valor, extrato = extrato)
        saldo = retorno[0]
        extrato = retorno[1]
        
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        retorno = saque(saldo = saldo, valor = valor, extrato = extrato, limite = limite, numero_saques = numero_saques, limite_saques = LIMITE_SAQUES)
        saldo = retorno [0]
        extrato = retorno[1]
        numero_saques = retorno[2]

    elif opcao == "e":
        imprimir_extrato(saldo, extrato = extrato)

    elif opcao == "n":
        criar_novo_usuario();

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")