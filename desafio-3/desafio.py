import re

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[n] Cadastrar Novo Usuário 
[c] Cadastrar Nova Conta

=> """

usuarios = {}
limite = 500
saldo = 0
extrato = ""
contas_usuarios = []
conta = 1
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

def busca_usuario():
    global usuarios
    cpf = re.sub(r'\D', '', input("Digite o CPF do novo usuário: \n"))
    usuario = usuarios.get(cpf)
    return usuario, cpf

def criar_novo_usuario():
    endereco = "Endereço não informado"
    usuario, cpf = busca_usuario()
    
    if usuario is not None:
        print("Usuário já foi cadastrado no sistema")
        return None
    
    nome = input('Digite o nome completo: \n')
    data_nascimento = input("Digite a data de nascimento no formato dd/MM/aa :\n")

    if(input("Cadastrar endereço: (S ou N): \n").lower() == "s"):
        endereco = cadastrar_endereco()
    
    usuario = {"nome":nome, "data de nascimento": data_nascimento, "endereço": endereco }
    print(f'Usuário cpf: {cpf} foi cadastrado com sucesso: \n {usuario}')
    return cpf, usuario
      
def cadastrar_endereco():
    logradouro = input("Digite o logradouro: \n")
    nro = ", " + input("Digite o número do imóvel: \n") 
    bairro = " - " +  input("Digite o bairro: \n") 
    cidade = input("Digite a cidade: \n")
    estado = "/" + input("Digite a sigla do estado: \n").upper()

    return logradouro + nro + bairro + " " + cidade + estado

def criar_nova_conta(*,conta, saldo, extrato,cpf):
    nova_conta = {"agencia"     : "0001" , 
                  "numero_conta": conta  ,
                  "saldo"       : saldo  ,
                  "extrato"     : extrato,
                  "cpf"         : cpf     }
    
    return nova_conta
    
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
        dados_usuario = criar_novo_usuario()
        if dados_usuario is not None:
            cpf, usuario = dados_usuario
            usuarios[cpf] = usuario

    elif opcao == "c":
        usuario = busca_usuario()
        print(usuario)
        if usuario[0] is None:
            print("Usuário não localizado")

        else:
            print("Flubber That!")
            nova_conta = criar_nova_conta(conta=conta, saldo=saldo, extrato=extrato, cpf=usuario[1]);
            contas_usuarios.append(nova_conta)
            print(contas_usuarios)
            conta += 1

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")