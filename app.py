from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
   weight = 0
   height = 0
   bmi = 0
   if request.method == 'POST' and 'weight' in request.form and 'height' in request.form:
      weight = request.form.get('weight')
      height = request.form.get('height')
      bmi = calcBmi(float(weight), float(height))
   return render_template("index.html",
                        bmi=bmi)

def calcBmi(weight, height):
   bodyMassIndex = 0
   heightInMeter = height/100
   bodyMassIndex = round((weight/(heightInMeter**2)),2)
   return bodyMassIndex

if __name__ == '__main__':
   app.run(debug=True)