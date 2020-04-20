from flask import Flask, flash, redirect, render_template, request, session, abort
rom config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def home():
    return render_template("index.html")



def get_db_connection():
    import sqlite3
    conn = sqlite3.connect('database/nba.db')
    conn.row_factory = sqlite3.Row

    return conn.cursor()


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=80)
    app.run(debug=True)