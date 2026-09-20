<div align="center">

# 💻 CS50x: Introduction to Computer Science

### *From "hello, world" in C to a full-stack web app — one problem set at a time.*

**Complete solutions to Harvard University's [CS50x](https://cs50.harvard.edu/x/), from C and memory management to Python, SQL, and full-stack web development with Flask.**

[![Harvard CS50x](https://img.shields.io/badge/Harvard-CS50x-A51C30?style=for-the-badge)](https://cs50.harvard.edu/x/)
[![C](https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white)](https://en.wikipedia.org/wiki/C_(programming_language))
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.sqlite.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Status](https://img.shields.io/badge/Problem%20Sets-All%20weeks-success?style=for-the-badge)](#-coursework)

[Overview](#-overview) · [Coursework](#-coursework) · [Highlights](#-highlighted-projects) · [Concept Map](#-concept--project-map) · [Getting Started](#-getting-started) · [Structure](#-repository-structure) · [Certificate](#-certificate) · [Honesty](#-academic-honesty)

</div>

---

## 📖 Overview

This repository contains my work for [CS50x](https://cs50.harvard.edu/x/) — Harvard's introduction to computer science and the art of programming. The course moves from low-level C and manual memory management to high-level Python and SQL, and finishes by building complete, database-backed web applications with Flask.

> [!TIP]
> **Final project:** [StudyTrack](#-studytrack-final-project), a full-stack study session tracker with user accounts, session logging, and an analytics dashboard.

| | |
|:---|:---|
| 🗣️ **Languages** | C, Python, SQL, JavaScript, HTML, CSS |
| 🧰 **Frameworks** | Flask, Jinja, Bootstrap |
| 🗄️ **Database** | SQLite |
| 🎯 **Final project** | [StudyTrack](#-studytrack-final-project), a full-stack study session tracker |
| 🎓 **Certificate** | Awarded 2026 |

---

## 🗂️ Coursework

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
| 10 | Final Project | `project` (StudyTrack) | Full-stack application design |

---

## 🌟 Highlighted Projects

### 📈 Finance: Full-Stack Stock Trading App

A web application where users register, log in, look up live stock quotes, buy and sell shares, and review their transaction history.

- **Features:** user authentication (hashed passwords + session cookies), portfolio tracking with live valuations, quote lookup, full transaction history
- **Stack:** Flask, SQLite, Jinja, Bootstrap, HTML/CSS
- **Location:** [`finance/`](finance/)

### 📊 StudyTrack: Final Project

A personal study tracker for logging and analyzing study sessions — designed, built, and shipped from scratch for Week 10.

- **Features:** registration and login, add/edit/delete sessions, analytics dashboard, responsive interface
- **Stack:** Flask, SQLite, HTML/CSS, JavaScript
- **Location:** [`project/`](project/)

### 🔤 Speller: Hash Table Spell Checker

Loads a dictionary into a hash table and checks text files for misspelled words — CS50's famous performance race, optimized for speed on large inputs.

- **Language:** C
- **Techniques:** hash tables, linked lists (chaining), file I/O, manual memory management with `malloc`/`free`
- **Location:** [`speller/`](speller/)

### 🧬 DNA: STR Matching

Identifies a person from a DNA sequence by counting Short Tandem Repeats (STRs) and matching the profile against a CSV database.

- **Language:** Python
- **Techniques:** file parsing, string matching, CSV handling
- **Location:** [`dna/`](dna/)

---

## 🗺️ Concept → Project Map

Where each core CS50 idea lives in this repository:

| Concept | Where You'll Find It | One-Line Essence |
|:--------|:---------------------|:-----------------|
| Greedy algorithms | `cash/`, `credit/` | Make the locally optimal choice at each step; validate card numbers with Luhn's |
| Cryptography basics | `caesar/` | Shift letters by a key — the oldest cipher in the book |
| Recursion & graphs | `tideman/` | Lock in pairwise election winners without creating cycles |
| Pointers & memory | `filter-less/`, `recover/` | Walk bytes directly to blur images and carve JPEGs from raw disk |
| Hash tables | `speller/` | O(1) average lookups turn spell-checking into a speed contest |
| File parsing | `dna/` | Count STR repeats and match them against a database |
| SQL joins | `fiftyville/` | Solve a mystery by joining suspects, calls, and flights |
| DOM manipulation | `trivia/` | Respond to clicks and check answers with JavaScript events |
| Sessions & auth | `finance/` | Keep users logged in and their data isolated per session |
| Full-stack design | `project/` | Routes, templates, and a database working as one app |

---

## 🛠️ Tech Stack

| Category | Technologies |
|:---------|:-------------|
| **Languages** | C, Python, SQL, JavaScript, HTML, CSS |
| **Frameworks** | Flask, Jinja, Bootstrap |
| **Databases** | SQLite |
| **Tools** | Git, GitHub, VS Code, Valgrind, debug50 |
| **Concepts** | Algorithms, Data Structures, Memory Management, Hash Tables, Graphs, SQL Joins, Web APIs |

---

## 🚀 Getting Started

### Prerequisites

- A C compiler (`clang` or `gcc`) and `make` for the C projects
- Python **3.9** or newer for the Python and Flask projects
- Flask (installed via `pip`) for the web projects

### Installation

```bash
git clone https://github.com/sonubiswal/CS50x-Work.git
cd CS50x-Work
```

### Running a Project

**C projects**

```bash
cd <project-name>
make <project-name>
./<project-name>
```

**Python projects**

```bash
cd <project-name>
python <file>.py
```

**Flask projects** (`finance`, `birthdays`, `project`)

```bash
cd <project-name>
pip install -r requirements.txt
flask run
```

<details>
<summary>💡 <b>Tips</b></summary>

- **C projects:** compile with `make` (which wraps `clang` with CS50's warning flags); run `help50` and `debug50` if available, and `valgrind ./speller` to check for memory leaks.
- **Finance / StudyTrack:** set the app environment with `export FLASK_APP=application.py` before `flask run` if the server doesn't start.
- **Databases:** SQLite files (`.db`) are included or created on first run — delete and re-run to reset to a clean state.

</details>

---

## 📁 Repository Structure

```text
.
├── scratch/                          # Week 0: Scratch
├── hello/                            # Week 1: C basics
├── mario-less/, mario-more/          # Week 1: Mario pyramids
├── cash/, credit/                    # Week 1: Greedy algorithms, Luhn
├── scrabble/, readability/, caesar/  # Week 2: Arrays
├── plurality/, runoff/, tideman/     # Week 3: Voting algorithms
├── filter-less/, filter-more/        # Week 4: Bitmap filters
├── recover/                          # Week 4: JPEG recovery
├── inheritance/                      # Week 5: Linked lists (family trees)
├── speller/                          # Week 5: Hash table spell checker
├── sentimental-hello/, sentimental-mario/    # Week 6: Python ports
├── sentimental-cash/, sentimental-readability/
├── dna/                              # Week 6: STR matching
├── songs/, movies/, fiftyville/      # Week 7: SQL
├── homepage/, trivia/                # Week 8: HTML, CSS, JavaScript
├── birthdays/                        # Week 9: Flask basics
├── finance/                          # Week 9: Stock trading app
└── project/                          # Week 10: StudyTrack (final project)
```

Each folder contains the problem set source; C folders also include the CS50 Makefile-compatible build setup, and Flask folders include `application.py` plus `requirements.txt`.

---

## 🎓 Certificate

**CS50x: Introduction to Computer Science**
Harvard University · Completed 2026

---

## 🤝 Academic Honesty

This repository is a record of my own learning, published to document how each problem set was understood and solved.

If you are currently taking CS50x, please follow the course's [Academic Honesty policy](https://cs50.harvard.edu/x/policy/#academic-honesty): do not copy this code. Use it only as reference after you have submitted your own work — the struggle is the point.

---

<div align="center">

**⭐ Built one problem set at a time.**

If you found this useful, consider giving it a star — it means a lot.

[![Star](https://img.shields.io/badge/%E2%AD%90_Star-CS50x--Work-FFD700?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sonubiswal/CS50x-Work)

Made with 💻 and ☕ · 10 weeks · 6 languages · 1 final project

</div>
