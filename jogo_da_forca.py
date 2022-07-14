import os
import math
op = 0
score = 0
while op != 4:
  def txt():
    print(":::::::::::::::\Jogo da Forca/:::::::::::::::")
  def lin():
    a = w*1.5
    b = '='*math.ceil(a)
    return b
  txt()
  print()
  print('[1] Nova partida\n[2] Pontuações\n[3] Informações do jogo\n[4] Sair')
  op = int(input("O que deseja fazer? --> "))  
  
  word = '  '
  hidden_word = []
  l_errada = []
  erro = 0
  acerto = 0
  os.system('cls')

  if op == 1:
    os.system('cls')
    txt() 
    word = input("Digite a palavra: ")
    word = word.lower()
    w = len(word)
    dica = input("Dê uma dica: ")
    for letra in word:
      hidden_word.append('*')
      
    while acerto < w:
        os.system('cls')
        txt()
        print(f'{lin()}|PONTUAÇÃO: {score}|{lin()}')
        print(f'{lin()}|Palavra escondida|{lin()}\n{hidden_word}')
        print('----|Quantidade de letra da palavra:',w,'|----')
        print('Dica:',dica)
        print('Erros:',l_errada)
        l = input("Digite uma letra: ")
        l = l.lower()

        for indice, letra in enumerate(word):
          if l == letra:
              l_caps = l.upper()
              hidden_word[indice] = l_caps
              acerto += 1

        if acerto == w//2:
          os.system('cls')
          print('Você acaba de ter chance de acertar a palavra inteira!\n [1] Sim [2] Não')
          chance = int(input('Deseja tentar?: '))
          while chance != 2:
            if chance == 1:
              c_unica = input("Digite a palvra: ")
              if c_unica == word:
                score = (score + 15)-5
                acerto = w
                break
              else:
                erro = 5
                score -= 5
                if score < 0:
                  score = 0
                break

        if l not in word:
              l_errada.append(l) 
              erro += 1
        if erro >= 5:
            print("Você perdeu!")
            break
        print()
        
        if acerto == w:
          score = score + 5
          if erro >= 1:
            score -= erro
          print('Você acertou a palavra. Parabéns!')

  if op == 2:
    print('Pontuação:',score)
  if op ==3:
      os.system('cls')
      print('----------|Informações sobre o game|-----------')
      print('Ojetivo: Acertar a palavra escondida')
      print('Chances: Você tem 5 vidas, caso erre 5 letras\nperderá a partida')
      print('Chance única: Caso acerte a palavra na \nchance única +15 pontos, se errar -5 pontos')
      print('Pontuação: Se conseguir acertar a palavra\nsem errar +5 pontos a cada letra errada -1 ponto')
      print('-'*45)

print("Fim :P")