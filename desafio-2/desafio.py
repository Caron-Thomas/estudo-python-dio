# Limite de 10 transações por dia (saque ou deposito)(Ok)  
# Extrato deve mostrar data e hora de todas as transações(Ok) TODO melhorar frontão (Ok)

from datetime import datetime, timedelta
import pytz

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

mini_menu = """
    ou escolha uma das duas opões disponíveis abaixo:
    [e]\tExtrato
    [q]\tSair
    => """

saldo = 0
limite = 500
extrato = ""
numero_operacoes = 0
LIMITE_OPERACOES = 10
localidade = "America/Sao_Paulo"
HOJE = datetime.now(pytz.timezone(localidade))

def depositar(deposito, data):
    global saldo 
    global extrato
    global numero_operacoes
    
    if(not validar_numero_operacoes(funcao=True)):
        return "Boa tentativa, mas você já atingiu a cota de operações do dia!"

    saldo += deposito
    extrato = extrato + (f'deposito de R$ {deposito:.2f} {data}\n')
    numero_operacoes += 1
    return "Deposito efetuado com sucesso"

def sacar(saque, data):
    global saldo 
    global extrato
    global numero_operacoes

    if(not validar_numero_operacoes(funcao=True)):
        return "Estamos de olho, mesmo com saldo, pore gentileza, retorne amanhã!"
    
    if(saque > limite or saque > saldo):
        return "Valor escolhido para saque maior que o permitido, ou saldo insuficiente"
    
    saldo -= saque
    extrato = extrato + (f'saque    de R$ {saque:.2f} {data}\n')
    numero_operacoes += 1
    return "Saque efetuado com sucesso"

def validar_input_usuario(mensagem, funcao):
    mascara_ano_hora = "%d/%m/%Y %H:%M:%S"
    valor = float(input(mensagem))
    if(valor <= 0 or not valor.is_integer() ):
        print("Operações devem ser valores positivos, inteiros, e válidos") 

    else:
        agora = datetime.strftime(datetime.now(pytz.timezone(localidade)),mascara_ano_hora)
        print(funcao(int(valor), agora))

def validar_numero_operacoes(funcao=False):
    operacoes_restam_no_dia = LIMITE_OPERACOES - numero_operacoes
    mascara_ano = "%d/%m/%Y"
    
    if(operacoes_restam_no_dia <= 0):
        print("Limite diário de operações atingidos. Por gentileza, volte amanhã")
        return False
    
    if(not funcao):
        print(f'Para o dia de hoje, {HOJE.strftime(mascara_ano)} ainda restam {operacoes_restam_no_dia} operações disponíves.')
    
    return True

while True:
    opcao = input(menu if validar_numero_operacoes() else mini_menu)

    if opcao == "d":
        print("Você escolheu depositar em sua conta")
        mensagem = "Entre com o valor a ser depositado: "
        validar_input_usuario(mensagem, depositar)

    elif opcao == "s":
        mensagem = "Entre com o valor inteiro a ser sacado: "
        validar_input_usuario(mensagem, sacar)

    elif opcao == "e":
        print(" extrato ".center(24,"-"))
        print("Não foram feitas operações até o momento" if not extrato else extrato) # Correção -> Caso nenhuma operação, imprimir saldo vazio 
        print(f'Saldo final da conta: R$ {saldo:.2f}')
        print("".center(24,"-"))

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

print(" Obrigado por utilizar o Banco Suzano!! ".center(45, "="))
