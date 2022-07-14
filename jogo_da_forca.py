import os
op = 0
while op != 3:
  def txt():
    print("::::::::::::\Jogo da Forca/::::::::::::")
  txt()
  print('[1] Nova partida\n[2] Ver pontuações\n[3] Sair')
  op = int(input("O que deseja fazer? --> "))  
  word = '  '
  hidden_word = []
  erro = 0
  acerto = 0
  os.system('cls')

  if op == 1:
    os.system('cls')
    txt()
    score = 0
    word = input("Digite a palavra: ")
    dica = input("Dê uma dica: ")
    for letra in word:
      hidden_word.append('*')

    while acerto < len(word):
        os.system('cls')
        txt()
        print('Pontuação:',score)
        print(f'Palavra escondida:\n{hidden_word}')
        print('Quantidade de letra da palavra:',len(word))
        print('Dica:',dica)
        l = input("Digite uma letra: ")

        for indice, letra in enumerate(word):
          if l == letra:
              hidden_word[indice] = l
              acerto += 1

        if l not in word:
              erro += 1
              if erro >= 6:
                print("Você perdeu!")
                break
        print('\n')
    if acerto == len(word):
        print('Você acertou a palavra. Parabéns!')

  if op == 2:
    print('Pontuação:',score)
print("Fim :P")