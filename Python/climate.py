from flask import Flask, url_for, render_template, request, redirect
import json

app = Flask(__name__)


@app.route('/index/', methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')
    #return '<h1>Climate Inc. Version {}</h1>'.format(version)
@app.route('/index/urmomgay/', methods=['GET', 'POST'])
def hoi():
    return '<h1> urmomgay </h1>'

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