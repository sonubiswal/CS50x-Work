from datetime import date
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, parse_session_form
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
db = SQL("sqlite:///studytrack.db")
db.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        hash TEXT NOT NULL)""")
db.execute("""CREATE TABLE IF NOT EXISTS sessions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        subject TEXT NOT NULL,
        minutes INTEGER NOT NULL,
        studied_on TEXT NOT NULL,
        notes TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id))""")
@app.after_request
def no_cache(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response
@app.route("/")
@login_required
def index():
    rows = db.execute(
        "SELECT * FROM sessions WHERE user_id = ? ORDER BY studied_on DESC, id DESC",
        session["user_id"],
    )
    return render_template("index.html", sessions=rows)
@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    if request.method == "POST":
        data, error = parse_session_form(request.form)
        if error:
            return apology(error)

        db.execute(
            "INSERT INTO sessions (user_id, subject, minutes, studied_on, notes) VALUES (?, ?, ?, ?, ?)",
            session["user_id"], data["subject"], data["minutes"], data["studied_on"], data["notes"],
        )
        flash("Session added.")
        return redirect("/")

    return render_template("add.html", today=date.today().isoformat())
@app.route("/edit/<int:session_id>", methods=["GET", "POST"])
@login_required
def edit(session_id):
    rows = db.execute(
        "SELECT * FROM sessions WHERE id = ? AND user_id = ?",
        session_id, session["user_id"],
    )
    if not rows:
        return apology("Session not found.", 404)

    if request.method == "POST":
        data, error = parse_session_form(request.form)
        if error:
            return apology(error)

        db.execute(
            "UPDATE sessions SET subject = ?, minutes = ?, studied_on = ?, notes = ? WHERE id = ? AND user_id = ?",
            data["subject"], data["minutes"], data["studied_on"], data["notes"],
            session_id, session["user_id"],
        )
        flash("Session updated.")
        return redirect("/")

    return render_template("edit.html", s=rows[0])
@app.route("/delete/<int:session_id>", methods=["POST"])
@login_required
def delete(session_id):
    db.execute(
        "DELETE FROM sessions WHERE id = ? AND user_id = ?",
        session_id, session["user_id"],
    )
    flash("Session deleted.")
    return redirect("/")
@app.route("/dashboard")
@login_required
def dashboard():
    rows = db.execute(
        "SELECT subject, SUM(minutes) AS total FROM sessions WHERE user_id = ? GROUP BY subject ORDER BY total DESC",
        session["user_id"],
    )
    grand_total = sum(r["total"] for r in rows)
    return render_template("dashboard.html", rows=rows, grand_total=grand_total)
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        confirmation = request.form.get("confirmation", "")

        if not username:
            return apology("Please choose a username.")
        if not password:
            return apology("Please choose a password.")
        if password != confirmation:
            return apology("Passwords do not match.")

        existing = db.execute("SELECT id FROM users WHERE username = ?", username)
        if existing:
            return apology("That username is already taken.")

        db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)",
            username, generate_password_hash(password),
        )
        row = db.execute("SELECT id FROM users WHERE username = ?", username)
        session["user_id"] = row[0]["id"]
        flash("Welcome to StudyTrack!")
        return redirect("/")

    return render_template("register.html")
@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if not username:
            return apology("Please enter your username.", 403)
        if not password:
            return apology("Please enter your password.", 403)

        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            return apology("Invalid username or password.", 403)

        session["user_id"] = rows[0]["id"]
        return redirect("/")
    return render_template("login.html")
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")
