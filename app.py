from flask import Flask, render_template, request
from model import predictDisease

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/predict', methods = ['POST', 'GET'])
def predict():
    if request.method == 'GET':
        return render_template('predict.html', res = "", info = "")
    else:
        symp1 = request.form['symp1']
        symp2 = request.form['symp2']
        
        symp3 = "null"
        symp4 = "null"
        symp5 = "null"
        symp6 = "null"
        
        if(request.form['symp3'] != ""):
            symp3 = request.form['symp3']
        if(request.form['symp4'] != ""):
            symp4 = request.form['symp4']
        if(request.form['symp5'] != ""):
            symp5 = request.form['symp5']
        if(request.form['symp6'] != ""):
            symp6 = request.form['symp6']

        data = "{},{},{},{},{},{}".format(symp1,symp2, symp3,symp4, symp5, symp6)
        
        info = data.split(",")
        
        result = predictDisease(data)
        return render_template('predict.html', result = result , info = info)
        

if(__name__ == "__main__"):
    app.run(debug=True)