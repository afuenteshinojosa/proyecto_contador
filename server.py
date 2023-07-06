from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'MyScretKey'

@app.route("/")
def root():
    if ("visitas" in session):
        session["visitas"] += 1
    else:
        session["visitas"] = 0
    return render_template('index.html')


@app.route("/clear")
def clear():
    session.clear()
    return redirect("/")

@app.route("/sumar")
def sumar():
    session["visitas"] += 1
    return redirect("/")

@app.route("/destroy_session")
def destroy_session():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True, port= 5002)