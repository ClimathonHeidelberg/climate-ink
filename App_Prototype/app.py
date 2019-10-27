from flask import Flask, url_for, render_template, request, redirect
import json
from game import Game
import numpy as np

app = Flask(__name__)

data = {}
data['temp'] = 0.6
data['year'] = 2019
data['plot_temp'] = 'plot_temp.png'
with open('output_game.txt', 'w') as outfile:
    json.dump(data, outfile)

@app.route('/index/', methods=['GET', 'POST'])
def hello_world():
    with open('output_game.txt') as json_file:
        data = json.load(json_file)
        temperature = np.round(data['temp'], 3)
        year = data['year']
    context = {'temp': temperature, 'year': year}
    return render_template('index.html', variable=context)
    #return '<h1>Climate Inc. Version {}</h1>'.format(version)
@app.route('/index/urmomgay/', methods=['GET', 'POST'])
def hoi():
    return '<h1> urmomgay </h1>'

@app.route('/start/', methods=['GET', 'POST'])
def startGame():
    print('start_game')
    data={}
    data['coal']= None
    data['traffic']= None

    game = Game()
    game.play()
    

@app.route('/handle_data', methods=['POST'])
def handle_data():
    years = request.form.get('exitYears')
    AreThereCars = int(request.form.get('AreThereStillCars'))
    data={}
    data['coal'] = years
    data['traffic'] = AreThereCars
    
    with open('data.text','w') as outfile:
        json.dump(data,outfile)
    return redirect('/index')
    # return a response
    
if __name__== "__main__":
    app.run()