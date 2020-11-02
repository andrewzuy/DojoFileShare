from flask import Flask, render_template, request, send_from_directory, redirect
import os
path = os.getcwd()+"/share"

list_of_files = {}
flask_app = Flask(__name__)

def get_files():
    return os.listdir(path)

@flask_app.route("/")
def index():
   return render_template("index.html", files = get_files())

@flask_app.route('/share/<path:path>')
def send_js(path):
    return send_from_directory('share', path)

@flask_app.route("/upload", methods=["POST"])
def upload():
    file = request.files['file']
    file.save(flask_app.root_path+"/share/"+file.filename)
    return redirect("/")

def exit():
    raise RuntimeError('Not running with the Werkzeug Server')