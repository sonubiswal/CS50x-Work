# StudyTrack

#### Video Demo: https://www.youtube.com/watch?v=x_o3alKYbig

#### Description:

A small web app written in Flask and SQLite to help students track study time. It was born out of frustration with the long process of recording in a notebook or keeping track of spreadsheets when I would study for 2 hours every couple of days and by Friday had no idea where that time had gone. I wanted something simple to log a session and give me a clear picture of what happened where.

## What It Does

A user can register an account, log in, and track sessions. Each session has 4 fields: subject, minutes, date, and optional note. Once sessions have been added, a user can view them on their home page with options to edit or delete any listed, and see a dashboard with all their time grouped by subject.

Some notes on the implementation:

- All sessions are scoped to the current user. Any query that reads, edits, or deletes includes `user_id = ?` in the `WHERE` clause. So a user can't tamper with the URL to modify someone else's sessions.
- Subjects are lower-cased in the DB so 'Math' and 'math' and 'MATH' will be grouped together in the dashboard rather than appearing as 3 different subjects. They are displayed in title case in the app itself.
- Dates are stored as ISO strings for simplicity. This makes them easily sortable as text without having to do any parsing, and it avoids ambiguity.
- Validation logic is all in a shared helper so the add and edit routes don't diverge. If a rule changes, it's only updated in one place.
- The homepage lists a user's sessions in a table. The dashboard shows the same data but aggregated.

## Files

- **app.py** – The app itself. Sets up the routes, connects to the DB, and creates tables if needed at server start. Has an `after_request` handler that sets no-cache headers so browsers don't show cached versions of the homepage after a session edit or delete.
- **helpers.py** – Shared functions. `apology(message, code)` renders an error page with the given message and HTTP status code. `login_required` is a decorator that redirects to `/login` if there's no current user. `parse_session_form()` parses and validates form submissions.
- **templates/** – All Jinja files. `layout.html` is the master page, other pages extend it. `index.html` is the homepage with a list of sessions. `add.html` and `edit.html` are self-explanatory. `dashboard.html` is the subject-aggregated view. `apology.html` is the error template. `login.html` and `register.html` are for user auth.
- **static/** – `styles.css` for presentation. `script.js` adds a confirmation dialog to all delete forms so accidental deletes are prevented.
- **studytrack.db** – The SQLite database file. It must exist before the app starts; the tables are created inside it on first run.
- **requirements.txt** – Packages the project needs: `cs50`, `flask`, `flask-session`, and `werkzeug`.

## Design Decisions

One of the bigger ones was where to put validation logic for adding and editing sessions. Early on I had duplicated code in both routes checking if the subject was empty, that the minutes was an integer, that it wasn't negative or over 24 hours, and so on. It worked, but it was obviously a maintenance burden waiting to happen. So I pulled it all into a helper function, `parse_session_form()`, which either returns a parsed and validated dict or an error message. Both the add and edit routes call it the same way.

I went with filesystem-based sessions via `flask-session` rather than the default cookie-based sessions. The default session stores its data in the cookie itself, which is signed to prevent tampering but still visible to the client. For this app that would have been fine, since the only thing in the session is a user id, but I preferred keeping session data on the server so that if I ever added something more sensitive later I wouldn't have to rethink the whole thing.

For the database layer I used CS50's `SQL` class, which provides a helpful wrapper around `sqlite3`. It does parameterized queries so I don't have to worry about SQL injection, and it returns rows as dicts, which made writing the templates easier. There's no ORM layer because it wasn't needed; raw SQL is straightforward enough for this project.

One decision I'm not as happy about is that the dashboard is read-only. It wouldn't be that hard to add edit and delete links to each row there, but I worried it would bloat the page and make it less approachable. The dashboard is a high-level overview, the homepage is for detailed editing, and if someone wants to edit a session they can always go to the homepage.

## Testing

I tested the app manually through several scenarios. I registered two separate accounts and confirmed that the second could not edit or delete the first user's sessions by guessing an id in the URL; those requests returned the "Session not found" page. I checked that the delete confirmation popup appears and that cancelling it leaves the row in place. I also tested the empty states on both the homepage and the dashboard by logging in as a fresh user with no sessions, and confirmed that friendly messages appear instead of empty tables. On the validation side I tried submitting an empty subject, non-numeric minutes, negative and over-1440 minutes, an impossible date, and a future date, and confirmed each produced the correct error.
