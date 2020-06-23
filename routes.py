from flask import Flask, request, render_template, jsonify
import json
import numpy as np
import pickle
#logre=joblib.load('jsonmodel.pkl')

ip=open("srinivas",'rb')
m=pickle.load(ip)
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')
'''
@app.route('/submit',methods=['POST'])
def fun():
	if request.method == 'POST':
		data=request.form
		global h
		h=float(request.form['height'])
		global w
		w=float(request.form['weight'])
		global ge
		ge=request.form['gender']
		if ge=='male':
			return render_template('home2.html')
		else:
			return render_template('home.html')	'''

@app.route('/Submit',methods=['POST'])
def Submit():
	if request.method == 'POST':	
		data=request.form
		#print(data)
		'''if ge=='male':
			preg=0
		else:
			preg = int(request.form['Pregnancies'])
		print(preg)'''
		gluc = float(request.form['opening'])
		bp = float(request.form['high'])                
		st = float(request.form['low'])                
		iss = float(request.form['close'])
		#hi=0.3048*h                
		#bmi= w/(hi*hi)  
		#print(bmi)              
		dpf=float(request.form['volume'])                		
		#age=int(request.form['Age'])
		k=[[gluc,bp,st,iss,dpf]]                
		pred=m.predict(k) 
		print(pred)
		'''if pred == [0.]:
			p="NEGATIVE"
		else:
			p="POSITIVE"


		if p=="POSITIVE":
			return render_template('res1.html')
		else:
			return render_template('result.html')'''
		return str(float(pred))


if __name__ == '__main__':
  app.run(debug=True)