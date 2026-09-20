import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    rows = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    cash = rows[0]["cash"]

    # Wrap in a try-except block to handle cases where the transactions table hasn't been created yet
    try:
        holdings = db.execute("""
            SELECT symbol, SUM(shares) AS shares
            FROM transactions
            WHERE user_id = ?
            GROUP BY symbol
            HAVING SUM(shares) > 0
        """, session["user_id"])
    except Exception:
        holdings = []

    portfolio = []
    total_value = 0
    for h in holdings:
        stock = lookup(h["symbol"])
        if stock is None:
            continue
        value = stock["price"] * h["shares"]
        total_value += value
        portfolio.append({
            "symbol": h["symbol"],
            "shares": h["shares"],
            "price": stock["price"],
            "value": value
        })

    grand_total = cash + total_value
    return render_template("index.html", cash=cash, portfolio=portfolio, total=grand_total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not symbol:
            return apology("must provide symbol", 400)

        try:
            shares = int(shares)
        except (ValueError, TypeError):
            return apology("shares must be a positive integer", 400)

        if shares <= 0:
            return apology("shares must be a positive integer", 400)

        stock = lookup(symbol.upper())
        if stock is None:
            return apology("invalid symbol", 400)

        rows = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = rows[0]["cash"]
        total_cost = stock["price"] * shares

        if cash < total_cost:
            return apology("can't afford", 400)

        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?",
                   total_cost, session["user_id"])
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
                   session["user_id"], stock["symbol"], shares, stock["price"])

        flash("Bought!")
        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    try:
        transactions = db.execute("""
            SELECT symbol, shares, price, timestamp
            FROM transactions
            WHERE user_id = ?
            ORDER BY timestamp DESC
        """, session["user_id"])
    except Exception:
        transactions = []
    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username:
            return apology("must provide username", 403)
        if not password:
            return apology("must provide password", 403)

        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            return apology("invalid username and/or password", 403)

        session["user_id"] = rows[0]["id"]
        return redirect("/")
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""
    session.clear()
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("must provide symbol", 400)

        stock = lookup(symbol.upper())
        if stock is None:
            return apology("invalid symbol", 400)

        return render_template("quoted.html", stock=stock)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("must provide username", 400)
        if not password:
            return apology("must provide password", 400)
        if password != confirmation:
            return apology("passwords must match", 400)

        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(rows) != 0:
            return apology("username already taken", 400)

        hash_val = generate_password_hash(password)
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash_val)

        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        session["user_id"] = rows[0]["id"]
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not symbol:
            return apology("must provide symbol", 400)

        try:
            shares = int(shares)
        except (ValueError, TypeError):
            return apology("shares must be a positive integer", 400)

        if shares <= 0:
            return apology("shares must be a positive integer", 400)

        rows = db.execute("""
            SELECT SUM(shares) AS total FROM transactions
            WHERE user_id = ? AND symbol = ?
        """, session["user_id"], symbol)
        owned = rows[0]["total"] or 0

        if shares > owned:
            return apology("too many shares", 400)

        stock = lookup(symbol.upper())
        if stock is None:
            return apology("invalid symbol", 400)

        total_value = stock["price"] * shares

        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?",
                   total_value, session["user_id"])
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
                   session["user_id"], stock["symbol"], -shares, stock["price"])

        flash("Sold!")
        return redirect("/")
    else:
        # Fixed: Filter out symbols by checking SUM(shares) > 0 instead of filtering raw logs
        try:
            rows = db.execute("""
                SELECT symbol FROM transactions
                WHERE user_id = ?
                GROUP BY symbol
                HAVING SUM(shares) > 0
            """, session["user_id"])
        except Exception:
            rows = []
        return render_template("sell.html", symbols=rows)


@app.route("/password", methods=["GET", "POST"])
@login_required
def password():
    """Change password (personal touch)"""
    if request.method == "POST":
        current = request.form.get("current")
        new = request.form.get("new")
        confirmation = request.form.get("confirmation")

        if not current or not new or not confirmation:
            return apology("fill all fields", 400)
        if new != confirmation:
            return apology("passwords must match", 400)

        rows = db.execute("SELECT hash FROM users WHERE id = ?", session["user_id"])
        if not check_password_hash(rows[0]["hash"], current):
            return apology("incorrect current password", 400)

        new_hash = generate_password_hash(new)
        db.execute("UPDATE users SET hash = ? WHERE id = ?", new_hash, session["user_id"])

        flash("Password changed!")
        return redirect("/")
    else:
        return render_template("password.html")
