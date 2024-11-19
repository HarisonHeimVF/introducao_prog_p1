tipo_animal = input(
    'Seu animal favorito é mamífero ou réptil? ').strip().lower()

print('Seu animal favorito pode ser um cachorro!' if tipo_animal ==
      'mamífero' else 'Seu animal favorito pode ser uma tartaruga!' if tipo_animal == 'réptil' else 'Resposta inválida!')
