from flask import Flask
from flask import request, url_for, redirect, session, render_template

app = Flask("firstFormApplication")
app.secret_key = "very_important_secret"


@app.route("/employees")
def display_employees():
    employees = ["John", "Bob", "Henry", "Alice", "Alan"]
    return render_template("employees.html", employees=employees)


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.run(host="0.0.0.0", port=8080, debug=True)
