#  Implement user sessions in a Flask app to store and display user-specific data.
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Set a secret key for session encryption

@app.route('/')
def index():
    return "Welcome to my Flask app!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        # You can validate the user here (e.g., check credentials in a database)
        session['username'] = username
        return redirect(url_for('profile'))
    return render_template('index5.html')

@app.route('/profile')
def profile():
    username = session.get('username')
    if username:
        return f"Hello, {username}! This is your profile."
    return "Please log in first."

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0" , port=5005)