from flask import Flask, redirect, url_for,render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/")
def players():
    return render_template("players.html")


@app.route("/")
def gameData():
    return render_template("gameData.html")

@app.route("/")
def shopping():
    return render_template("shopping.html")

@app.route("/")
def teams():
    return render_template("teams.html")

#@app.route("/<name>")
#def user(name):
  #  return f"Hello {name}!"


#@app.route("/admin/")
#def admin():

   # return redirect(url_for("user",name="Admin!"))


if __name__ == "__main__":
    app.run()
