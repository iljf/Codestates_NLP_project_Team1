from flask import Flask
from flask import Flask, render_template
from flask import request
import torch
from transformers import RobertaForSequenceClassification
from transformers import AutoTokenizer
from module import MODEL, pre_treat
import math

### pre_load ###
if torch.cuda.is_available():
    device = torch.device('cuda')
else:
    device = torch.device('cpu')

model = MODEL("/Users/damon/Documents/pre_onboarding/assignment3/checkpoint","klue/roberta-base")

app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
        
def Train():
    if request.method == 'POST':
 
        sentence1 = pre_treat(request.form['Sentence1'])
        sentence2 = pre_treat(request.form['Sentence2'])

        output = model.forward(request.form['Sentence1'],request.form['Sentence2'])
        #predition

        pred = round(output[0].item(), 1)
        pred1 = math.trunc(pred*20)
        label = '두 문장이 유사합니다.' if pred>=3.0 else '두 문장이 유사하지 않습니다.' 
    return render_template('result.html', gen=label, sen1=sentence1, sen2=sentence2, data1=pred1)

if __name__ == '__main__': 
    app.run(debug=True)
