## Desafio: Otimizando um Sistema Bancário com Funções Python

Este projeto propõe a otimização de um sistema bancário simples, refatorando suas operações em funções dedicadas e aprimorando a gestão de usuários e contas.

### Enunciado

O desafio consiste em implementar as seguintes funcionalidades:

#### 1. Funções de Operação Bancária

Refatore as operações de saque, depósito e extrato em funções separadas, cada uma com seus próprios requisitos de argumentos.

* **saque**: Deve receber os argumentos apenas por **palavra-chave** (`keyword only`).
    * **Parâmetros:** `saldo`, `valor`, `extrato`, `limite`, `numero_saques`, `limite_saques`.
    * **Retorno:** O saldo atualizado e o extrato da operação.

* **deposito**: Deve receber os argumentos apenas por **posição** (`positional only`).
    * **Parâmetros:** `saldo`, `valor`, `extrato`.
    * **Retorno:** O saldo atualizado e o extrato da operação.

* **extrato**: Deve receber o primeiro argumento por **posição** e o segundo por **palavra-chave**.
    * **Parâmetros:** `saldo` (posicional) e `extrato` (nomeado).

#### 2. Funções de Cadastro

Crie novas funções para gerenciar o cadastro de usuários e contas bancárias, garantindo a unicidade e a estrutura dos dados.

* `cadastrar_usuario`:
    * **Dados necessários:** nome, data de nascimento, CPF e endereço.
    * **Formato do endereço:** `logradouro, nro - bairro - cidade/sigla estado`.
    * **Requisito:** O CPF deve ser um valor único e conter apenas números.

* `cadastrar_conta`:
    * **Dados necessários:** agência, número da conta e usuário.
    * **Detalhes:** A agência deve ser fixa (`0001`), o número da conta deve ser sequencial, e a relação entre usuário e conta deve ser de um para muitos (`1:N`), permitindo que um usuário tenha múltiplas contas.