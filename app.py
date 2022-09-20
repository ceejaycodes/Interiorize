import os
import time
import datetime
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required, lookup

# Configure application
app = Flask(__name__)


# Ensure that api key in exported
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")



# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///interiorize.db")


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
    return render_template("index.html")


@app.route("/shops", methods=['GET','POST'])
@login_required
def shops():
    return render_template("shops.html")
    
    
@app.route("/sofas", methods=['GET','POST'])
@login_required
def sofas():
    if request.method == 'POST':
        address = request.form.get("address")
        locate = lookup(address)
        if not address:
           flash("please input an address")
           render_template("sofas.html")
        elif locate == None:
            flash("sorry! We don't always get what we want")
            return render_template("sofas.html")
        return render_template("sofas2.html" ,address = address, locate = locate)
    else:
        return render_template("sofas.html")
    
    
@app.route("/chairs", methods=['GET','POST'])
@login_required
def chairs():
    if request.method == 'POST':
        address = request.form.get("address")
        locate = lookup(address)
        if not address:
           flash("please input an address")
           render_template("chairs.html")
        elif locate == None:
            flash("sorry! We don't always get what we want")
            return render_template("chairs.html")
        return render_template("chairs2.html" ,address = address, locate = locate)
    else:
        return render_template("chairs.html")
    
    
@app.route("/tables", methods=['GET','POST'])
@login_required
def tables():
    if request.method == 'POST':
        address = request.form.get("address")
        locate = lookup(address)
        if not address:
           flash("please input an address")
           render_template("tables.html")
        elif locate == None:
            flash("sorry! We don't always get what we want")
            return render_template("tables.html")
        return render_template("tables2.html" ,address = address, locate = locate)
    else:
        return render_template("tables.html")
    
    
@app.route("/shelves", methods=['GET','POST'])
@login_required
def shelves():
    if request.method == 'POST':
        address = request.form.get("address")
        locate = lookup(address)
        if not address:
           flash("please input an address")
           render_template("shelves.html")
        elif locate == None:
            flash("sorry! We don't always get what we want")
            return render_template("shelves.html")
        return render_template("shelves2.html" ,address = address, locate = locate)
    else:
        return render_template("shelves.html")
    
    
@app.route("/register", methods=['GET','POST'])
def register():
    session.clear()  # clear current session.

    if request.method == "POST":

        username = request.form.get("username")
        email = request.form.get("email")
        password = generate_password_hash(request.form.get("password"))

        # Ensure username was submitted
        if not username:
            flash("must provide username", "error")
            return render_template("register.html")
            
        if not email:
            flash("must provide email", "error")
            return render_template("register.html")

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("must provide password", 'error')
            return render_template("register.html")

        # confirm password submitted
        elif not request.form.get("confirmation"):
            flash("must confirm password", "error")
            return render_template("register.html")

        # check if password and confirm password match
        elif not request.form.get("password") == request.form.get("confirmation"):
            flash("password do not match")
            return render_template("register.html")

        # check if username already exists, if not,add username and password to database
        try:
            db.execute("INSERT INTO users (username, email, password) VALUES (?,?,?)", username, email, password)
        except:
            flash("Username/email Exists Already")
            return render_template("register.html")
        else:
            users = db.execute("SELECT * FROM users WHERE username = ?", username)
            session["user_id"] = users[0]["id"]
            return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html") 
    
    
    
@app.route("/login", methods=['GET','POST'])
def login():
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            flash("must provide username")
            return render_template("login.html")
            

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("must provide password")
            return render_template("login.html")

        # Query database for username data
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        if len(rows) == 1 and check_password_hash(rows[0]["password"], request.form.get("password")):
            session["user_id"] = rows[0]["id"]
            return redirect("/")
        else:
            code = 405
            flash ("incorrect username/password combination")
            return render_template("login.html")

    else:
        return render_template("login.html")
    
    
@app.route("/logout")
# @login_required
def logout():
    session.clear()
    return render_template("index.html")


@app.route("/contact", methods=['GET','POST'])
@login_required
def contact():
    if request.method == 'POST': 
        name = request.form.get("name")
        message = request.form.get("message")
        try:
            db.execute("INSERT INTO contact(user_id, name, message) VALUES(?,?,?)", session["user_id"], name, message)
            flash("Message Sent!")
            return render_template("index.html")
        except:
            return render_template("error.html")

    else:
        return render_template("contact.html")
    

@app.route("/about")
@login_required
def about():
    return render_template("about.html")