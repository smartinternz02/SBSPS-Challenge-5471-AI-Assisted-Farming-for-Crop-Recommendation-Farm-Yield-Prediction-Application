import re
from flask import Flask,render_template,request

app=Flask(__name__)
@app.route('/crop_prediction')
def home():
    return render_template('home.html')

@app.route('/output')
def output():
    return render_template('output.html')
    
if __name__=="__main__":
    app.run()