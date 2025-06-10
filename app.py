from flask import Flask , request ,render_template, redirect, url_for
from werkzeug.utils import secure_filename
import pandas as pd
import matplotlib.pyplot as plt
import io ,os
import base64

UPLOAD_FOLDER=os.path.join(os.path.dirname(__file__),'uploads')

ALLOWED_EXTENTIONS={'csv'}

os.makedirs(UPLOAD_FOLDER,exist_ok=True)

app=Flask(__name__)
app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER

def allowed_file(filename):
    return "." in filename and filename.rsplit(".",1)[1].lower()=="csv"

@app.route("/")
def index():
    
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)