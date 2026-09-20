<div align="center">

# 💻 CS50x: Introduction to Computer Science

*From "hello, world" in C to a full-stack web app, one problem set at a time.*

[![Harvard CS50x](https://img.shields.io/badge/Harvard-CS50x-A51C30?style=for-the-badge)](https://cs50.harvard.edu/x/)
[![C](https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white)](https://en.wikipedia.org/wiki/C_(programming_language))
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

[Overview](#overview) · [Coursework](#coursework) · [Featured Projects](#featured-projects) · [Concept Map](#concept-map) · [Getting Started](#getting-started) · [Structure](#repository-structure) · [Certificate](#certificate)

</div>

---

## Overview

My work for [CS50x](https://cs50.harvard.edu/x/), Harvard's introduction to computer science. The course starts with low-level C and manual memory management, moves through Python, SQL, and the web, and ends with building a complete database-backed application.

| | |
|:---|:---|
| 🗣️ **Languages** | C, Python, SQL, JavaScript, HTML, CSS |
| 🧰 **Frameworks and libraries** | Flask, Jinja, Bootstrap |
| 🗄️ **Database** | SQLite |
| 🔧 **Tools** | Git, GitHub, VS Code, Valgrind, debug50 |
| 📚 **Topics** | Algorithms, data structures, memory management, hash tables, graphs, SQL joins, web APIs |
| 🎯 **Final project** | [StudyTrack](#studytrack), a full-stack study session tracker |
| 🎓 **Certificate** | Completed 2026 |

---

## Coursework

| Week | Topic | Projects | Key Concepts |
|:----:|:------|:---------|:-------------|
| 0 | Scratch | `scratch` | Visual programming, events, loops |
| 1 | C | `hello`, `mario-less`, `mario-more`, `cash`, `credit` | Loops, greedy algorithms, Luhn's algorithm |
| 2 | Arrays | `scrabble`, `readability`, `caesar` | Strings, arrays, basic cryptography |
| 3 | Algorithms | `plurality`, `runoff`, `tideman` | Voting systems, recursion, graph theory |
| 4 | Memory | `filter-less`, `filter-more`, `recover` | Pointers, bitmap processing, JPEG recovery |
| 5 | Data Structures | `inheritance`, `speller` | Linked lists, hash tables, dynamic memory |
| 6 | Python | `sentimental-hello`, `sentimental-mario`, `sentimental-cash`, `sentimental-readability`, `dna` | Python syntax, file parsing, CSV handling |
| 7 | SQL | `songs`, `movies`, `fiftyville` | Queries, joins, relational databases |
| 8 | HTML, CSS, JavaScript | `homepage`, `trivia` | Layout, styling, DOM manipulation |
| 9 | Flask | `birthdays`, `finance` | Routing, sessions, templates, authentication |
| 10 | Final Project | `project` | Full-stack application design |

---

## Featured Projects

### StudyTrack

> **Final project** · Flask · SQLite · HTML/CSS · JavaScript · [`project/`](project/)

A personal study tracker for logging and analyzing study sessions, designed and built from scratch.

- User registration and login
- Add, edit, and delete study sessions
- Analytics dashboard
- Responsive interface

### Finance

> **Week 9** · Flask · SQLite · Jinja · Bootstrap · [`finance/`](finance/)

A stock trading web app where users register, look up live quotes, buy and sell shares, and review their history.

- Authentication with hashed passwords and session cookies
- Portfolio tracking with live valuations
- Full transaction history

### Speller

> **Week 5** · C · [`speller/`](speller/)

A spell checker that loads a dictionary into a hash table and scans text files for misspelled words, tuned for speed on large inputs.

- Hash table with linked-list chaining
- File I/O and manual memory management with `malloc` and `free`
- Checked for leaks with Valgrind

### DNA

> **Week 6** · Python · [`dna/`](dna/)

Identifies a person from a DNA sequence by counting Short Tandem Repeats (STRs) and matching the profile against a CSV database.

- File parsing and string matching
- CSV handling

---

## Concept Map

Where each core CS50 idea lives in this repository:

| Concept | Project | What it demonstrates |
|:--------|:--------|:---------------------|
| Greedy algorithms | `cash/`, `credit/` | Locally optimal choices, plus card validation with Luhn's algorithm |
| Cryptography basics | `caesar/` | Shifting letters by a key |
| Recursion and graphs | `tideman/` | Locking in pairwise election winners without creating cycles |
| Pointers and memory | `filter-less/`, `recover/` | Working with raw bytes to blur images and carve JPEGs from a disk image |
| Hash tables | `speller/` | Constant-time average lookups for fast spell-checking |
| File parsing | `dna/` | Counting STR repeats and matching them against a database |
| SQL joins | `fiftyville/` | Solving a mystery by joining suspects, calls, and flights |
| DOM manipulation | `trivia/` | Handling click events and checking answers in JavaScript |
| Sessions and auth | `finance/` | Keeping users logged in with their data isolated |
| Full-stack design | `project/` | Routes, templates, and a database working as one app |

---

## Getting Started

### Prerequisites

- A C compiler (`clang` or `gcc`) and `make` for the C projects
- Python 3.9 or newer for the Python and Flask projects

### Installation

```bash
git clone https://github.com/sonubiswal/CS50x-Work.git
cd CS50x-Work
```

### Running a project

**C**

```bash
cd <project-name>
make <project-name>
./<project-name>
```

**Python**

```bash
cd <project-name>
python <file>.py
```

**Flask** (`finance`, `birthdays`, `project`)

```bash
cd <project-name>
pip install -r requirements.txt
flask run
```

<details>
<summary><b>Troubleshooting tips</b></summary>

- **C projects:** run `valgrind ./speller` to check for memory leaks, and use `debug50` or `help50` when tracking down bugs.
- **Flask projects:** run `flask run` from inside the project folder so Flask can find the app.
- **Databases:** SQLite files (`.db`) are included or created on first run. Delete the file and re-run to reset to a clean state.

</details>

---

## Repository Structure

```text
.
├── scratch/                     Week 0   Scratch
├── hello/                       Week 1   C basics
├── mario-less/  mario-more/     Week 1   Mario pyramids
├── cash/  credit/               Week 1   Greedy algorithms, Luhn
├── scrabble/  readability/      Week 2   Arrays
│   caesar/
├── plurality/  runoff/          Week 3   Voting algorithms
│   tideman/
├── filter-less/  filter-more/   Week 4   Bitmap filters
├── recover/                     Week 4   JPEG recovery
├── inheritance/                 Week 5   Linked lists
├── speller/                     Week 5   Hash table spell checker
├── sentimental-*/               Week 6   Python ports of C problems
├── dna/                         Week 6   STR matching
├── songs/  movies/              Week 7   SQL
│   fiftyville/
├── homepage/  trivia/           Week 8   HTML, CSS, JavaScript
├── birthdays/                   Week 9   Flask basics
├── finance/                     Week 9   Stock trading app
└── project/                     Week 10  StudyTrack (final project)
```

Each folder holds the problem set source. Flask projects also include a `requirements.txt`.

---

## Certificate

**CS50x: Introduction to Computer Science**
Harvard University · Completed 2026

---

## Academic Honesty

This repository documents my own learning. If you are currently taking CS50x, please follow the course's [Academic Honesty policy](https://cs50.harvard.edu/x/policy/#academic-honesty) and use this code for reference only, after you have submitted your own work.

---

<div align="center">

**Built one problem set at a time.**

[![GitHub](https://img.shields.io/badge/GitHub-sonubiswal-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sonubiswal)

If this was useful, consider giving the repo a star.

</div>
