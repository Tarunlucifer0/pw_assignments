#Develop a Flask app that uses URL parameters to display dynamic content.

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to my dynamic Flask app!"

@app.route('/greet')
def greet():
    data=request.args.get("name")
    return f"hello ! {data}"
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002)
