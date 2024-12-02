from flask import Flask,render_template,request
import pickle
import numpy as np
# import register_login
model = pickle.load(open('model12.pkl','rb')) 
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict',methods =['POST'])
def placement(): 
        Age = int(request.form.get('Age'))
        Sex= int(request.form.get('Sex')) 
        ChestPainType = int(request.form.get('ChestPainType')) 
        RestingBP=int(request.form.get('RestingBP'))
        Cholesterol =int(request.form.get('Cholesterol'))
        FastingBS= int(request.form.get('FastingBS'))
        RestingECG= int(request.form.get('RestingECG'))
        MaxHR =int(request.form.get('MaxHR'))
        ExerciseAngina =int(request.form.get('ExerciseAngina'))
        Oldpeak=float(request.form.get('Oldpeak'))
        ST_Slope=int(request.form.get('ST_Slope'))
        # # ST_Slope_Up= int(request.form.get('ca'))
        # RestingECG= int(request.form.get('RestingECG'))
        # # RestingECG_ST= int(request.form.get('slope'))
        # ASY= int(request.form.get('ASY'))
        # ATA= int(request.form.get('ATA'))
        # NAP= int(request.form.get('NAP'))
        # TA= int(request.form.get('TA'))
#        Age,Sex,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope,HeartDisease
# 0,40,0,140,289,0,5,172,0,0.0,2,0
        result = model.predict(np.array([[Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope]]))
        print(f"{result=}")
        if result[0] == 1:
            result = "POSITIVE"
        else:
            result ="NEGATIVE"
        # return render_template('index.html',prediction = register_login.register_user(result))
        return render_template('index.html',prediction = result)

if __name__ == '__main__':
    app.run(host= '0.0.0.0',port = 8080, debug=True)



















    #, dtype=np.float64
