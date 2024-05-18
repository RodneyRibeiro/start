'''
DESAFIO:
Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para verificar, à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.

ENTRADA:
A entrada consiste de vários casos de teste. A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste. Cada caso de teste consiste de dois valores A e B maiores que zero, cada um deles podendo ter até 1000 dígitos.

SAÍDA:
Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no primeiro valor, confome exemplo abaixo.
'''

#variáveis
saldo = 1000.0
saques_total=3
extrato = []

while True:
    #Menu aparece todas as vezes que sai da opção selecionada.
    print ("""
       [1] Saque
       [2] Deposito
       [3] Extrato
       [4] Sair
       """)
    #Seleção do menu
    menu = int(input())
    #Menu Saque ---------------------------------------------------------------------------
    if menu == 1:
       print ("Saque\n")
       print ("Digite o Valor para Saque:\n")
       #Round para garantir que o saldo tenha 2 dígitos após a vírgula
       saque = round(float(input()),2)
       #Prevenção de valores negativos
       if saque < 0:
           print ("Valor digitado é inválido. Digite um valor positivo")
       #Limite de saque 500
       elif saque > 500:
           print ("Valor de saque excede o máximo permitido.(500)")
       #Testar se não há saldo    
       elif saque >= saldo and saques_total > 0:
           print ("Não há saldo")
       #Condição que o saque seja menor que o Saque e que esteja dentro dos 3 saques disponíveis
       elif saque <= saldo and saques_total > 0:
           saldo = saldo - saque
           saques_total -= 1
           extrato.append("Saque: R$"+str(saque) + " Saldo: R$" + str(saldo))
           print (f"Seu saldo é de R${saldo} e ainda possui {saques_total} saques hoje.")
       elif saques_total == 0:
           print ("Limite de Saques Atingido.")
    #Menu Depósito --------------------------------------------------------------------------
    elif menu == 2:
       print ("Depósito")
       print ("Digite o Valor para Depósito:\n")
       #Round para garantir que o saldo tenha 2 dígitos após a vírgula
       deposito = round(float(input()),2)
       #Prevenção de valores negativos ou igual a 0
       if deposito <= 0:
           print ("Valor digitado é inválido. Digite um valor positivo")
       elif saque <= saldo and saques_total > 0:
           saldo = saldo + deposito
           extrato.append("Deposito: R$"+str(saque) + " Saldo: R$" + str(saldo))
           print (f"Seu saldo é de R${saldo}.")
    #Menu Extrato ---------------------------------------------------------------------------
    elif menu == 3:
       print ("Extrato")
       print (extrato)
    #Menu Sair ------------------------------------------------------------------------------
    elif menu == 4:
       print ("Obrigado por ser nosso cliente.")
       break
    #Prevenção de erro-----------------------------------------------------------------------
    else:
       print ("Opção Incorreta, tente de novo.")
   
