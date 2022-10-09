from flask import Flask, redirect, url_for, render_template, request, session, flash, jsonify
import secrets
import ScheduledMessenger
import csv
import json
import pandas
from pandas import *
from time import sleep

# Set Flask secret key
app = Flask(__name__)
app.secret_key = secrets.token_bytes()

# Read the .json config file
with open("config.json", "r") as json_config:
    config = json.load(json_config)

# Define stylesheet
@app.route("/stylesheet.css")
def css():
    return redirect(url_for('static', filename='stylesheet.css'))

# Login page
@app.route("/", methods=["POST", "GET"])
def auth():
    if "user" in session:
        return redirect(url_for("home"))
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == config["USERNAME"] and password == config["PASSWORD"]:
            session["user"] = username
        return redirect(url_for("home"))
    else:
        return render_template("auth.html")

# Run WA-ScheduledMessenger
@app.route("/run")
def send():
    if "user" not in session:
        return redirect(url_for("auth"))
    ScheduledMessenger.main()
    return render_template("/home.html")

# View the .csv file
@app.route("/schedule")
def schedule():
    if "user" not in session:
        return redirect(url_for("auth"))
    schedule = read_csv(config["DATE_FILENAME"], low_memory=False)
    return render_template("schedule.html", schedule=schedule)

# Append data to .csv
@app.route("/append", methods=["POST", "GET"])
def append():
    if "user" not in session:
        return redirect(url_for("auth"))
    schedule = read_csv(config["DATE_FILENAME"])

    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        date = request.form["date"]
        message = request.form["message"]
        with open(config["DATE_FILENAME"], "a") as schedule:
            schedule.write(f"\n{name},{phone},{date},{message}")
        return redirect(url_for("append"))
    return render_template("append.html", schedule=schedule)

# Erase the schedule
@app.route("/erase")
def erase():
    if "user" not in session:
        return redirect(url_for("auth"))
    with open(config["DATE_FILENAME"], "w") as schedule:
        schedule.write("Name,Phone,Date,Message")
    return redirect(url_for("schedule"))

# Logout
@app.route("/logout")
def logout():
    session.pop("user")
    return redirect(url_for("auth"))

# Render homepage
@app.route("/home")
def home():
    if "user" not in session:
        return redirect(url_for("auth"))
    return render_template("home.html")

# Run WA-ScheduledMessenger daily
@app.route("/daily")
def daily():
    ScheduledMessenger.main()
    sleep(86380)
    daily()
    return render_template("/home")

# View the history (log file)
@app.route("/history")
def history():
    try:
        with open(config["SUCCESSFUL_MESSAGE_LOG"], "r") as file_log:
            history = file_log.read()
            if history == "":
                history = "No History"
    except:
        history = "No History"
    return render_template("history.html", history=history)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=2160)