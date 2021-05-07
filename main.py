from flask import Flask, render_template, url_for, request,send_from_directory

app = Flask('__name__')

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


    print(result, var_in)

    return render_template('game-choise.html')


@app.route('/result_game', methods = ['POST', 'GET'])
def result_game():
  if request.method == 'POST':
    result = request.form
    var_word = result['word']
    var_dip = result['dip']


    print(result, var_word, var_dip)

    return render_template('result-game.html')


if __name__ == '__main__':
  #app.run(host='0.0.0.0', port=8080, debug=True)
  app.run(host='127.0.0.1', port=8000, debug=True)
