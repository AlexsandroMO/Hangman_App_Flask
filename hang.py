  
import random
from tinydb import TinyDB, Query, where
#print('\n' * 500)
#print('WELCOME TO THE HANGMAN GAME!\n')

words_random = ['HOME','DOG','PYTHON','LYON','LIZARD','CHIP','APPLE','WOMAN']
dips_random = ['where people live','Animal','Animal','Animal','Animal','means of transport','fruit',"who's really in charge"]

# test = input('Do you intend to play alone [A] or with someone [S]?\n= ').upper()
# secret_word, dip = '',''

""" if test == 'S':
  secret_word = input('Tipe the secret word: ').upper()
  dip = input('Dip: ').upper()
elif test == 'A':
  num = random.randint(0, 7)
  secret_word = words_random[num]
  dip = dips_random[num]
else:
  print('Please, choice the a optis [S/A] and try again.')
  exit()
 """
#-----------------------------------------------------------
def tow_gamers(var_word, var_dip):
  lines = '_ ' * len(var_word)
  word = lines.split()

  print('\n' * 500)
  print('Discovery word') 
  print('{} with {} letter'.format(var_dip, len(var_word)))
  print(word)
  print('\n')

  result = ''

  return result

  # while life > 0:
  #   letter = input('= ').upper()

  #   dados = []
  #   for a in range(0, len(var_wordd)):
  #     if var_word[a] == letter:
  #       word[a] = letter
  #     else:
  #       dados.append('empyt')

  #   #------------------------- Teste de Derrota
  #   if len(dados) == len(var_word):
  #     life -= 1

  #   if life == 0:
  #     print('\n' * 500)
  #     result = 'Game Over!\n\nCreated by A.M.O'
  #   #------------------------- Teste de Vitória
  #   dados2 = []
  #   for i in word:
  #     if i == '_':
  #       dados2.append('X')
        
  #   if len(dados2) == 0:
  #     life = 0
  #     result = 'You Win!!!\n\nCreated by A.M.O'
  #   #-------------------------
  #   print('\n' * 500)
  #   print('RESULT            LIFE {}'.format(life), '\n')
  #   print('{} with {} letter\n'.format(dip, len(var_wordd)))
  #   print(word)
  #   print('\n{}'.format(result))
  #   print('\n\n')


  
""" 
data = {
  'word': CASA,
}

dbg.insert(data) """

""" 
data = {
  'life': 3,
  'word': 'CASA'
}

db.insert(data) """
# def zera_life():

#   l_db.clear_cache()
#   level = {
#     'life': 3
#   }

#   l_db.insert(level)
#   life = l_db.all()[0]['life']

#   return life




'''data = {
  'word': 'CADEIRA',
  'dip': 'OBJETO',
}

db_G.insert(data)'''


'''class ldb():
  def __init__(self, life):
    self.level = life

class game_AI():
  def __init__(self, word):
    self.secret = word'''
    


'''@app.route('/game_choise2', methods = ['POST', 'GET'])
def game_choise2():
  if request.method == 'POST':
    result = request.form
    var_in = result['select']

    if var_in == '1':
      AI = g_db.all()
      x = random.randint(0, 7)
      var_secret = AI[x]
      print('>>>------', x, AI[x])

      var_dip = var_secret['dip']

      len_var_word = len(var_secret['word'])
      lines = '_ ' * len(var_secret['word'])
      read_word  = lines.split()
      word = ''
      return render_template('game-choise3.html', word=word, var_dip=var_dip, len_var_word=len_var_word, var_secret=var_secret, read_word=read_word)

    else:
      return redirect(url_for('index'))
'''