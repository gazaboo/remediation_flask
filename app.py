from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/gallery")
def gallery():
    file_names = os.listdir('static/assets/')
    
    files_path = []
    for file in file_names:
        path = '../static/assets/' + file
        files_path.append(path)

    app.logger.info(files_path)
    return render_template('gallery.html', mes_fichiers=files_path, a=0)
