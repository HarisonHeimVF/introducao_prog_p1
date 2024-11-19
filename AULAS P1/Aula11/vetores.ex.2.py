notas = []
for i in range(5):
    while True:
        try:
            nota = float(input(f'Digite a nota do aluno {i + 1}:'))
            if 0<= nota <= 10:
                notas.append(nota)
                break
            else:
                print('A nota deve estar entre 0 e 10. Tente novamente')
        except ValueError:
            print('Entrada Inválida! Digite um número.')

media = sum(notas) / len(notas)

acima_media = len([nota for nota in notas if nota > media])


print(f'Média da turma: {media:2f}')
print(f'Alunos com nota acima da média: {acima_media}')