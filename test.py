from flask import Flask, render_template, request
import requests

api = "AIzaSyAwCz9qh2d8geT2y_I3H5Lcy5Z0Yp66-Io"

endpoint = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api}'

headers = {
    "Content-type" : "application/json"
}

app = Flask(__name__)

@app.route("/")
def awal():
    return render_template("index.html")

@app.route("/gemini-api", methods = ["POST"])
def gemini_api():
    input = request.form['data']
    data = {"contents": [{"parts":[{"text": input}]}]}
    response = requests.post(endpoint, headers=headers, json=data)
    if (response.status_code == 200):
        response_data = response.json()
        hasil = response_data['candidates'][0]['content']['parts'][0]['text']
        return{"msg":"Success", "bot_reply":hasil}

    
    return{"msg":"Failed"}

app.run()