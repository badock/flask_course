from flask import Flask
from flask import request, url_for, redirect, session, render_template
import json
app = Flask("firstFormApplication")
app.secret_key = "very_important_secret"

COUNTER = 0

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/increment_counter")
def increment_counter():
    global COUNTER
    COUNTER += 1
    return json.dumps({
        "status": "OK"
    })

@app.route("/fetch_counter")
def fetch_counter():
    global COUNTER
    return json.dumps({
        "counter": COUNTER
    })

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.run(host="0.0.0.0", port=8080, debug=True)
