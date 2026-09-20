from datetime import date
from functools import wraps
from flask import redirect, render_template, session
def apology(message, code=400):
    return render_template("apology.html", code=code, message=message), code
def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not session.get("user_id"):
            return redirect("/login")
        return f(*args, **kwargs)
    return wrapper
def parse_session_form(form):
    subject = form.get("subject", "").strip()
    minutes = form.get("minutes", "").strip()
    studied_on = form.get("studied_on", "").strip()
    notes = form.get("notes", "").strip()
    if not subject:
        return None, "Please enter a subject."
    try:
        minutes = int(minutes)
    except ValueError:
        return None, "Minutes must be a whole number."
    if minutes <= 0:
        return None, "Minutes must be greater than zero."
    if minutes > 1440:
        return None, "Minutes cannot exceed 1440."
    if not studied_on:
        return None, "Please pick a date."

    try:
        parsed_date = date.fromisoformat(studied_on)
    except ValueError:
        return None, "Please enter a valid date."
    if parsed_date > date.today():
        return None, "Date can't be in the future."
    return {
        "subject": subject.lower(),
        "minutes": minutes,
        "studied_on": parsed_date.isoformat(),
        "notes": notes,
    }, None
