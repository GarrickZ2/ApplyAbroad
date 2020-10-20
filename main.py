from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from upload import *

app = Flask(__name__, static_folder="./")
app.config['SECRET_KEY'] = 'dee6fe43513344455aaa292134f6a7d8'


@app.route("/", methods=['post', 'get'])
def main():
    data = get_info()
    return render_template("index.html", data=data)


@app.route("/upload", methods=['post', 'get'])
def upload():
    return render_template("upload.html")


@app.route("/submit", methods=['post', 'get'])
def submit():
    data = request.form.to_dict()
    upload_info(data['university'], data['program'], data['program_index'], data['apply'], data['language']
                , data['require'], data['recommend'], data['start'], data['end'])
    return redirect(url_for("upload"))


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
