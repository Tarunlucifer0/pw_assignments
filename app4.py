#Q4  Create a Flask app with a form that accepts user input and displays it.
from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index4.html')

@app.route("/data", methods =["POST", "GET"])
def greet():
    user_name=request.form.get("user_name")
    qualification=request.form.get("qualification")
    Age=request.form.get("Age")
    return f"user_name: {user_name}  User's Qualifiction:{qualification}  User's Age:{Age} "
    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5004)