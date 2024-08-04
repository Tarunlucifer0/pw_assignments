#1
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

if __name__=="__main__":
    app.run(host="0.0.0.0")


#2 Build a Flask app with static HTML pages and navigate between them
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



#3Develop a Flask app that uses URL parameters to display dynamic content.

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



#6
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route("/")
def index():
    return render_template("index6.html")

@app.route("/upload", methods=["POST", "GET"])
def upload():
    filet = request.files["file"]  # Use square brackets instead of parentheses
    filename = os.path.join(app.config['UPLOAD_FOLDER'], filet.filename)
    filet.save(filename)
    return redirect(url_for('uploaded_file', filename=filename))


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return f"Uploaded file: {filename}"  


if __name__=="__main__":
    app.run(host="0.0.0.0", port=5006)


#7
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL



app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crud'

mysql = MySQL(app)



@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM students")
    data = cur.fetchall()
    cur.close()




    return render_template('index2.html', students=data )



@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
        mysql.connection.commit()
        return redirect(url_for('Index'))




@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))





@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE students
               SET name=%s, email=%s, phone=%s
               WHERE id=%s
            """, (name, email, phone, id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002)