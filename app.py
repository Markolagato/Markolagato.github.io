import os

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

#from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def home():
    """Show home page"""

    return render_template("home.html")

@app.route("/menu", methods=["GET", "POST"])
def menu():
    """Show menu page"""

    return render_template("menu.html")

@app.route("/shop", methods=["GET", "POST"])
def shop():
    """Show shop page"""

    return render_template("shop.html")

@app.route("/restoration", methods=["GET", "POST"])
def restoration():
    """Show restoration page"""

    return render_template("restoration.html")
