  
import random

print('\n' * 500)
print('WELCOME TO THE HANGMAN GAME!\n')

words_random = ['HOME','DOG','PYTHON','LYON','LIZARD','CHIP','APPLE','WOMAN']
dips_random = ['where people live','Animal','Animal','Animal','Animal','means of transport','fruit',"who's really in charge"]

test = input('Do you intend to play alone [A] or with someone [S]?\n= ').upper()
secret_word, dip = '',''

if test == 'S':
  secret_word = input('Tipe the secret word: ').upper()
  dip = input('Dip: ').upper()
elif test == 'A':
  num = random.randint(0, 7)
  secret_word = words_random[num]
  dip = dips_random[num]
else:
  print('Please, choice the a optis [S/A] and try again.')
  exit()
#-----------------------------------------------------------

lines = '_ ' * len(secret_word)
word = lines.split()

print('\n' * 500)
print('Discovery word') 
print('{} with {} letter'.format(dip, len(secret_word)))
print(word)
print('\n')

life = 4
result = ''

while life > 0:
  letter = input('= ').upper()

  dados = []
  for a in range(0, len(secret_word)):
    if secret_word[a] == letter:
      word[a] = letter
    else:
      dados.append('empyt')

  #------------------------- Teste de Derrota
  if len(dados) == len(secret_word):
    life -= 1

  if life == 0:
    print('\n' * 500)
    result = 'Game Over!\n\nCreated by A.M.O'
  #------------------------- Teste de Vitória
  dados2 = []
  for i in word:
    if i == '_':
      dados2.append('X')
      
  if len(dados2) == 0:
    life = 0
    result = 'You Win!!!\n\nCreated by A.M.O'
  #-------------------------
  print('\n' * 500)
  print('RESULT            LIFE {}'.format(life), '\n')
  print('{} with {} letter\n'.format(dip, len(secret_word)))
  print(word)
  print('\n{}'.format(result))
  print('\n\n')