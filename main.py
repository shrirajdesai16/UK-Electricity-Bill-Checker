

from flask import Flask,render_template

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('templates/index.html')

@app.route('/result',methods = ['POST', 'GET'])
def calorie():
    if request.method == 'POST':
        unit = request.form['units']
        units = float(unit)
        if(units>0 and units<=100):
            payAmount=units*price_per_unit
        elif(units>100 and units<=200):
            payAmount=units*price_per_unit
        elif(units>200 and units<=500):
            payAmount=units*price_per_unit
        elif(units>500):
            payAmount=units*price_per_unit
        else:
             payAmount=0;

        Total= ( payAmount+standing_charge + vat )
        Total = Total / 103.25
        show = "Your Total Standing Charge for Month is" , standing_charge/103.25
        show = 'Consumed '+str(units)+' Units ','from',my_string, "to", my_string_1 ,+'\tBill Amount '+str(Total)
        return show
    else:
        return 'Sorry !!'
     

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port= 10250)