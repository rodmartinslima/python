#Variáveis
valorSalario = 1.00
listaSalarios = []
valorAbono = 0.00
somaAbono = 0.00
listaAbono = []
valorMinimo = 0.00
valorMaximoAbono = 0.00
qtdSalarioProcessado = 0
qtdMinimaColaboradores = 0
#Fim da lista de variaveis

# -- Início do Bloco de código - Teste de alteração para commit

"""
  O bloco de código abaixo obtém o valor de salário e cálcula o
  valor de abono....

  Teste alteração do script
"""

while (valorSalario != 0):
    valorSalario = float(input('Digite o valor do salário: '))
    listaSalarios.append(valorSalario)
    valorAbono = valorSalario * 20 * 1 / 100

    if (valorAbono < 100):
        valorAbono = 100.00
        
    listaAbono.append(valorAbono)
    qtdSalarioProcessado = qtdSalarioProcessado + 1

    if (valorSalario > 0):
        somaAbono = somaAbono + valorAbono

    if valorMinimo == 0 or valorSalario <= valorMinimo:
        if valorSalario < valorMinimo:
            qtdMinimaColaboradores = 0
            valorMinimo = valorSalario
            qtdMinimaColaboradores = qtdMinimaColaboradores + 1
        else:    
            valorMinimo = valorSalario
            qtdMinimaColaboradores = qtdMinimaColaboradores + 1

    if valorMaximoAbono == 0 or valorMaximoAbono <= valorAbono:
        valorMaximoAbono = valorAbono
else:
    print('\n Projeção de gastos com Abono')
    print('=========================================')

    for i in range(0, qtdSalarioProcessado - 1):       
        print('Salário: ', listaSalarios[i])

    print('\n Salário - Abono ')
    for i in range(0, qtdSalarioProcessado - 1):       
        print('Salário: ', listaSalarios[i], ' - ', listaAbono[i])

    print('\n')
    print('Foram processados', qtdSalarioProcessado - 1 ,'colaboradore(s)')
    print('Total gasto com abonos: ', somaAbono)
    print('Valor mínimo pago a ', qtdMinimaColaboradores ,'colaboradore(s)')
    print('Maior valor de abono pago: ', valorMaximoAbono)

# -- Fim do Bloco de código
