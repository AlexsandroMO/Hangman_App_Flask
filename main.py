#$ git config --global core.autocrlf input


from flask import Flask, render_template, url_for, redirect, request, send_from_directory
from tinydb import TinyDB, Query, where
import random

app = Flask('__name__')

#-----------------------------
db = TinyDB('DB/db.json')
db_G = TinyDB('DB/dbg.json')
#Ft = Query()

l_db = TinyDB('DB/db.json')
g_db = TinyDB('DB/dbg.json')
#-----------------------------

@app.route("/")
@app.route("/index")
def index():
  return render_template('index.html')


@app.route('/game_choise', methods = ['POST', 'GET'])
def game_choise():
  if request.method == 'POST':
    result = request.form
    var_in = result['select']

    print('tttt', var_in)

    if var_in == '2':
      l_db.update({'life': 0})
      # var_secret = ''
      # var_dip = ''
      # word = ''
      #return render_template('game-choise.html', word=word, var_secret=var_secret, var_dip=var_dip)
      return render_template('game-choise.html')

    else:
      return redirect(url_for('index'))


@app.route('/result_game', methods = ['POST', 'GET'])
def result_game():
  if request.method == 'POST':
    result = request.form
    var_word = result['word'].upper()
    var_dip = result['var-dip'].upper()
    #var_secret = result['var-secret']

    print('----------------------', var_dip)

    l_db.update({'life': 5})
    l_db.update({'word': var_word})

    len_var_word = len(var_word)
    lines = '_ ' * len(var_word)
    word = lines.split()
    return render_template('result-game.html', word=word, var_dip=var_dip, len_var_word=len_var_word) #var_secret=var_secret


@app.route('/result_game_play', methods = ['POST', 'GET'])
def result_game_play():
  if request.method == 'POST':
    result = request.form
    read_letter = result['letter'].upper()
    read_word = result['read-word']
    var_dip = result['var-dip'].upper()
    var_secret = result['var-secret']

    level = l_db.all()[0]['life']
    var_word = l_db.all()[0]['word']

    #---------------------------------
    read_word = read_word.replace('[','')
    read_word = read_word.replace(']','')
    read_word = read_word.replace("',",'')
    read_word = read_word.replace("'",'')
    read_word = read_word.split(' ')

    print('>>>>>>-->>>>>',  read_word, var_word, var_secret)

    len_var_word = len(var_word)
    dados = []
    for a in range(0, len(var_word)):
      if var_word[a] == read_letter:
        read_word[a] = read_letter

      else:
        dados.append('empyt')

      if len(dados) == len(var_word):
        l_db.update({'life': level -1})

    test_read_word = []
    for i in read_word:
      if i == '_':
        test_read_word.append('_')

    if len(test_read_word) == 0:
      return render_template('win.html')
    elif level > 0:
      return render_template('result-game-.html', read_word=read_word, var_dip=var_dip, len_var_word=len_var_word, var_secret=var_secret, level=level)
    else:
      return render_template('loose.html', var_word=var_word)


@app.route("/win")
def win():
  return render_template('win.html')


@app.route("/loose")
def loose():
  return render_template('loose.html')


if __name__ == '__main__':
  #app.run(host='0.0.0.0', port=8080, debug=True)
  app.run(host='127.0.0.1', port=8000, debug=True)
