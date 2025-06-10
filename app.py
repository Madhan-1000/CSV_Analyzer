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

@app.route("/linear-regression")
def linear_regression():
    return render_template("linear-regression/index.html")

@app.route("/linear_regression/upload",methods=["POST"])
def linear_upload():
    if "csv_file" not in request.files:
        return "No file part",400
    file=request.files["csv_file"]
    
    if file.filename=="":
        return "No Selected File",400
    if not allowed_file(file.filename):
        return "Only CSV files are allowed", 400
    
    filename=secure_filename(file.filename)
    filepath=os.path.join(app.config["UPLOAD_FOLDER"],filename)
    file.save(filepath)
    df=pd.read_csv(filepath)
    rows, cols = df.shape
    col_names = ', '.join(df.columns)

    return (
        f"""File uploaded successfully!
        Filename: {filename}
        Rows: {rows}
        Columns: {cols}
        Column Names: {col_names}"""
    )
if __name__=="__main__":
    app.run(debug=True)