nome_aluno = input('Olá aluno, digite seu nome :')
falta = float(input(nome_aluno + ' Insira sua quantidade de faltas: '))
if falta > 5:
    print('Sinto muito ' + nome_aluno + ' Voce foi Reprovado ' )
else:
    nota = float(input(nome_aluno + ' Insira a sua nota :'))
    if nota >= 6:
        print(nome_aluno + ' Parabéns, voce foi aprovado')
    else:
        print(nome_aluno + ' Voce foi reprovado')
