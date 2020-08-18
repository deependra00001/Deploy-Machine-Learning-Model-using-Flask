##Deploy a model as API

#Importing all the libraries
import numpy as np
import pickle
from flask import Flask, request,jsonify

def Predict_HousePrice_out(area):
    output = {'Predicted HousePrice is ':0}
    input_area=area
    filename='HousePricePredict_model.pkl'
    model=pickle.load(open(filename,'rb'))
    output['Predicted HousePrice is ']=model.predict([[input_area]])[0]
    #print(output)
    return output
# for testing above fuction
#Predict_HousePrice_out(3000)

app =Flask(__name__)
@app.route("/")
def index():
    return "House Price Prediction !"

@app.route("/HousePricePredict", methods = ["GET"])
def calc_HousePricePredict():
    body=request.get_data()
    header=request.headers
    
    try:
            num1 = int(request.args['area'])
            if(num1!=None):
                res=Predict_HousePrice_out(num1)
            else:
                    res={
                        'success': False,
                        'message': 'inputted data is not correct'
                        }
    except:
        res={
            'success': False,
            'message': 'Unknown error'
                }
    return jsonify(res)


if __name__=="__main__":
    app.run(debug=True, port=8791)
#http://127.0.0.1:8791/HousePricePredict?area=765