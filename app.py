from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile('config.cfg')

db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def home():
   result = BmiResults.query.all()
   return render_template('index.html',
                           result=result)
   

@app.route('/process', methods=['POST'])
def process():
   weight = 0
   height = 0
   name = ''
   bmi = 0
   if request.method == 'POST' and 'name' in request.form and 'weight' in request.form and 'height' in request.form:
      name = request.form.get('name')
      weight = request.form.get('weight')
      height = request.form.get('height')
      bmi = calcBmi(float(weight), float(height))

      bmiRes = BmiResults(name=name, bmi=bmi)
      db.session.add(bmiRes)
      db.session.commit()

   return redirect(url_for('home'))

@app.route('/delete')
def delete():
   obj = BmiResults.query.all()
   for j in obj:
      db.session.delete(j)
   db.session.commit()

   return redirect(url_for('home'))

def calcBmi(weight, height):
   bodyMassIndex = 0
   heightInMeter = height/100
   bodyMassIndex = round((weight/(heightInMeter**2)),2)
   return bodyMassIndex

class BmiResults(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(30))
   bmi = db.Column(db.Float)

if __name__ == '__main__':
   app.run(debug=True)