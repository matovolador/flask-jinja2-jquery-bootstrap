from flask import Flask, request,jsonify, make_response, render_template, send_from_directory, session
from flask_session import Session
from flask_cors import CORS
from flask_sslify import SSLify
import json
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = '123'
#CORS(app, supports_credentials=True)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.config['UPLOAD_FOLDER'] = "downloads"

@app.route("/",methods=["GET"])
def index():
    return render_template("index.html",message="Hello World!")

@app.route("/api/checkpermissions",methods=["GET"])
def token_metadata():
    if not session.get("user_id",False):
        return jsonify({
            "success": False,
            "message": "You must first login."
        })


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=5000)