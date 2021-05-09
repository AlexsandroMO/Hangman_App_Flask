#$ git config --global core.autocrlf input


from flask import Flask, render_template, url_for, request,send_from_directory
from tinydb import TinyDB, Query, where
import hang

app = Flask('__name__')

#-----------------------------
l_db = TinyDB('DB/db.json')
lft = Query()

life = 0
#-----------------------------

db = TinyDB('DB/db.json')
Ft = Query()

class ldb():
  def __init__(self, life):
    self.level = life



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



@app.route("/")
@app.route("/index")
def index():

  file = 'ok'

  return render_template('index.html', file=file)


@app.route('/game_choise', methods = ['POST', 'GET'])
def game_choise():
  if request.method == 'POST':
    result = request.form
    var_in = result['select']

    level = l_db.all()[0]['life']
    print('>>>>>>>>>>>>>', level, result, var_in)

    if var_in != '0':
      
      l_db.update({'life': 0})

      level = l_db.all()[0]['life']
      print('>>>>>>>=====', level)
      #level['life'] = var_in

    return render_template('game-choise.html')


@app.route('/result_game', methods = ['POST', 'GET'])
def result_game():
  if request.method == 'POST':
    result = request.form
    var_word = result['word'].upper()
    var_dip = result['dip'].upper()
    
    l_db.update({'life': 6})
    l_db.update({'word': var_word})
    #var_word = l_db.all()[0]['2']['word']

    len_var_word = len(var_word)
    lines = '_ ' * len(var_word)
    word = lines.split()

    return render_template('result-game.html', word=word, var_dip=var_dip, len_var_word=len_var_word)


@app.route('/result_game_test', methods = ['POST', 'GET'])
def result_game_test():
  if request.method == 'POST':
    result = request.form
    read_letter = result['letter'].upper()
    read_word = result['read-word']
    #var_dip = result['dip'].upper()

    var_dip = "dica" #<<<<<<<<<<<<<<<<<<<<<<<
    
    level = l_db.all()[0]['life']
    var_word = l_db.all()[0]['word']

    #---------------------------------
    read_word = read_word.replace('[','')
    read_word = read_word.replace(']','')
    read_word = read_word.replace("',",'')
    read_word = read_word.replace("'",'')
    read_word = read_word.split(' ')

    print('>>>>>>>>>>>', result, '----: ', read_word)

    len_var_word = len(var_word)

    dados = []
    for a in range(0, len(var_word)):
      if var_word[a] == read_letter:
        #print('----------------------->>', read_word[0], read_letter)
        read_word[a] = read_letter
        #read_word 
        #l_db.update({'word': read_letter})
      else:
        dados.append('empyt')
        #read_word[a] = '_'

    print('----------------------->>', read_word)

    return render_template('result-game-test.html', read_word=read_word, var_dip=var_dip, len_var_word=len_var_word, level=level)

    """ #------------------------- Teste de Derrota
    if len(dados) == len(var_word):
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
    print('{} with {} letter\n'.format(dip, len(var_wordd)))
    print(word)
    print('\n{}'.format(result))
    print('\n\n') """

    


if __name__ == '__main__':
  #app.run(host='0.0.0.0', port=8080, debug=True)
  app.run(host='127.0.0.1', port=8000, debug=True)
