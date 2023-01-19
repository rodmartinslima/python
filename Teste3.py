#Definição das listas com os nomes de alunos e notas para cada prova
NomeAlunos = ["Antônio Petrauski", "Beatriz Amorin", "Carla Santana","Humberto Magalhães","Sergio Mascarenhas","Raphael Back","Zélia"];
Prova01  = [3.0, 18.9, 2.3, 23.5, 12.5, 25.0, 10.0]
Prova02  = [4.5, 19.8, 3.2, 25.0, 13.7, 25.0, 18.5]
Prova03  = [23.8, 18.7, 1.7, 21.9, 14.7, 25.0, 17.9]
Prova04  = [12.0, 18.0, 13.5, 25.0, 16.9, 3.0, 24.5]

#declaração das variáveis
nLinhas = len(NomeAlunos)
notaMinima = []
notaMaxima = []
linha = '_'*72
mediaNotas = []
somaNotas = 0

#Publicar Cabeçalho __________________________________ 
print(linha)
print('{:^72s}'.format('Notas'))
print(linha)
print('{:^20s}{:^12s}{:^12s}{:^12s}{:^12s}'\
      .format('Estudante','Prova 1','Prova 2 ','Prova 3 ',  'Prova 4 '))
print(linha)
#final do cabeçalho

#tratamento dos valores mínimos, mmáximos e médias
for linhas in range(nLinhas):
    print('{:^20s}{:^12s}{:^12s}{:^12s}{:^12s}'\
          .format(NomeAlunos[linhas],str(Prova01[linhas]), str(Prova02[linhas]), str(Prova03[linhas]), str(Prova04[linhas])))
    notaMinima.append(min(Prova01[linhas], Prova02[linhas], Prova03[linhas], Prova04[linhas]))               
    notaMaxima.append(max(Prova01[linhas], Prova02[linhas], Prova03[linhas], Prova04[linhas]))
    somaNotas = Prova01[linhas] + Prova02[linhas] + Prova03[linhas] + Prova04[linhas]
    mediaNotas.append(somaNotas / 4)
    
#apresentação dos resultados
print(linha)
print()
print('{:^72s}'.format('Resultados'))
print(linha)
print()
for linhas in range(nLinhas):
    print(NomeAlunos[linhas])
    print('A nota mímima deste aluno foi: %10.2f' %(notaMinima[linhas]))
    print('A nota máxima deste aluno foi: %10.2f' %(notaMaxima[linhas]))
    print('A média final deste aluno foi: %10.2f' %(mediaNotas[linhas]))
    print(linha)
    print()
        
