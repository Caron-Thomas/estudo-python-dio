# depositar apenas valores postivios
# saque limitados a 3 por dia valor máximo de 500 e menor do que o saldo
# extrato deve listar todas as operações com o formato R$ xxx.xx e ao final, deverá ter o saldo.
# Pode ser apenas 1 usuário sem conta, sem Banco. Apenas o CPF

menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [n]\tNova conta
    [l]\tListar contas
    [u]\tNovo usuário
    [q]\tSair
    => """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(deposito):
    global saldo
    global extrato
 
    saldo += deposito
    extrato = extrato + (f'deposito de R$ {deposito:.2f}\n')

    return "Deposito efetuado com sucesso"

def sacar(saque):
    global saldo
    global extrato
    global numero_saques
    if(numero_saques >= LIMITE_SAQUES):
        return "Limite de saques diários atingidos. Por gentileza, volte amanhã"

    if(saque > limite or saque > saldo):
        return "Valor escolhido para saque maior que o permitido, ou saldo insuficiente"
    
    saldo -= saque
    extrato = extrato + (f'saque    de R$ {saque:.2f}\n')
    numero_saques += 1
    return "Saque efetuado com sucesso"

def validar_input_usuario(mensagem, funcao):
    valor = float(input(mensagem))
    if(valor <= 0 or not valor.is_integer() ):
        print("Depositos devem ser valores positivos, inteiros, e válidos") 

    else:
        print(funcao(int(valor)))

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Você escolheu depositar em sua conta")
        mensagem = "Entre com o valor a ser depositado: "
        validar_input_usuario(mensagem, depositar)

    elif opcao == "s":
        saques_restam_no_dia = LIMITE_SAQUES - numero_saques
        print(f'Você escolheu sacar de sua conta e ainda possui {saques_restam_no_dia} poerações para fazer hoje.')
        mensagem = "Entre com o valor inteiro a ser sacado: "
        validar_input_usuario(mensagem, sacar)

    elif opcao == "e":
        print(" extrato ".center(24,"-"))
        print(extrato)
        print(f'Saldo final da conta: R$ {saldo:.2f}')

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

print(" Obrigado por utilizar o Banco Suzano!! ".center(45, "="))
