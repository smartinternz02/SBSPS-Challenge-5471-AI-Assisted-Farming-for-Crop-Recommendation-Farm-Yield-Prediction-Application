from flask import Flask,render_template,request

app=Flask(__name__)
@app.route('/crop_prediction')
def home():
    return render_template('home.html')
    
if __name__=="__main__":
    app.run()