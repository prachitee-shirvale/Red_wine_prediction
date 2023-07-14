from flask import Flask,render_template,request, jsonify
import config
from wine_utils import Wine
app=Flask(__name__)

@app.route('/')
def homepage():
    return render_template('wine_webpage.html')

@app.route('/predict_quality', methods = ['GET', 'POST'])
def predict_quality():
    
    if request.method=='GET':
        data = request.args.get
        print("Data:",data)
        fixed_acidity= float(data('fixed_acidity'))
        volatile_acidity= float(data('volatile_acidity'))
        citric_acid= float(data('citric_acid'))
        residual_sugar= float(data('residual_sugar'))
        chlorides= float(data('chlorides'))
        free_sulfur_dioxide= float(data('free_sulfur_dioxide'))
        total_sulfur_dioxide= float(data('total_sulfur_dioxide'))
        pH= float(data('pH'))
        sulphates= float(data('sulphates'))
        alcohol= float(data('alcohol'))

        obj=Wine(fixed_acidity,volatile_acidity,citric_acid,residual_sugar,
                 chlorides,free_sulfur_dioxide,total_sulfur_dioxide,pH,sulphates,alcohol)
        predicted_quality = obj.get_predicted_quality()
    
        return render_template('wine_webpage.html', prediction = predicted_quality)
    
    elif request.method=='POST':
        data = request.form
        print("Data:",data)
        fixed_acidity= data['fixed_acidity']
        volatile_acidity= data['volatile_acidity']
        citric_acid= data['citric_acid']
        residual_sugar= data['residual_sugar']
        chlorides= data['chlorides']
        free_sulfur_dioxide= data['free_sulfur_dioxide']
        total_sulfur_dioxide= data['total_sulfur_dioxide']
        pH= data['pH']
        sulphates= data['sulphates']
        alcohol= data['alcohol']

        obj=Wine(fixed_acidity,volatile_acidity,citric_acid,residual_sugar,
                 chlorides,free_sulfur_dioxide,total_sulfur_dioxide,pH,sulphates,alcohol)
        predicted_quality = obj.get_predicted_quality()
    
        return render_template('wine_webpage.html', prediction = predicted_quality)
    return jsonify({"Message" : "Unsuccessful"})

if __name__=='__main__':
    app.run(host='0.0.0.0',port=config.PORT_NUMBER)