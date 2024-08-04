# Build a Flask app with static HTML pages and navigate between them
from flask import Flask ,render_template , request

app= Flask(__name__)

@app.route("/")
def home():
    return render_template('index2.html')

@app.route("/birthday", methods = ["POST"])
def surprise():
    return render_template('index3.html')




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)