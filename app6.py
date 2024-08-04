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