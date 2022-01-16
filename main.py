from flask import request,Flask,render_template
from flask_cors import cross_origin , CORS
from Log_Writer.logger import App_Logger
from Raw_Data_Formatter.data_formatter import formatter
from Data_Validator.data_validator import Validator
from Preprocessing.preprocessor import Preprocessor
from wsgiref import simple_server
import pickle
import sys
import os


app=Flask(__name__)
CORS(app)

log_writer=App_Logger()

@app.route('/',methods=['GET','POST'])
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/Prediction',methods=['POST'])
@cross_origin()
def index():

    try:
        if request.method=="POST":

            # Gathering the data and converting it to dataframe
            data = formatter().format_data()

            # Validating the input data
            err = Validator().validate(data)
            if err > 0:
                sys.exit()

            country = data.Country[0]

            # Preprocessing the data
            data = Preprocessor().preprocess(data)


            model=pickle.load(open("Model/xgboost_final.pickle","rb"))
            pred=model.predict(data)



            return render_template("results.html",country=country,prediction=pred[0])
        else :
            return render_template("index.html")

    except Exception as e:
        log_writer.log(log_message="Error Occurred in index page route")
        return print(e)



port = int(os.getenv("PORT",5000))
if __name__ == "__main__":
    host = '0.0.0.0'
    #port = 5000
    httpd = simple_server.make_server(host, port, app)
    # print("Serving on %s %d" % (host, port))
    httpd.serve_forever()


