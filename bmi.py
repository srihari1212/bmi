from pywebio.input import *
from pywebio.output import * 
from pywebio import start_server
from flask import Flask,render_template,request,make_response,jsonify
import os

app = Flask(__name__)

@app.route('/')
def bmicalculator():
    height = input("Enter your height in cm",type = FLOAT)
    weight = input("Enter your weight in kg",type = FLOAT)

    bmi = weight/(height/100)**2

    bmi_output=[(16, 'Severely underweight'), (18.5, 'Underweight'),
                  (25, 'Normal'), (30, 'Overweight'),
                  (35, 'Moderately obese'), (float('inf'), 'Severely obese')]
    for tuple1,tuple2 in bmi_output:
        if bmi<=tuple1:
            put_text('Your BMI is :%.1f and the person is :%s'%(bmi,tuple2))
            break



if __name__ == '__main__':
    app.run(debug=True)