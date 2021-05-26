import cs50
from flask import Flask,render_template

app = Flask(__name__)

db = cs50.SQL("sqlite:///corona_report.db")

@app.route("/")
def index():
    daily_affected = db.execute("SELECT DOE FROM shows WHERE status=1")
    affected = daily_affected.count({'DOE': '5/15/2020'})
    daily_recovered = db.execute("SELECT DOR FROM shows WHERE status=0")
    recovered = daily_recovered.count({'DOR': '5/15/2020'})
    daily_death = db.execute("SELECT DOD FROM shows WHERE status=2")
    death = daily_death.count({'DOD': '5/15/2020'})
    weekly_affected = db.execute("SELECT id FROM shows WHERE DOE BETWEEN '5/15/2020' AND '5/22/2020'")
    affectedw = len(weekly_affected)
    weekly_recovered = db.execute("SELECT id FROM shows WHERE DOR BETWEEN '5/15/2020' AND '5/22/2020'")
    recoveredw = len(weekly_recovered)
    weekly_death = db.execute("SELECT id FROM shows WHERE DOD BETWEEN '5/15/2020' AND '5/22/2020'")
    deathw = len(weekly_death)
    monthly_affected = db.execute("SELECT id FROM shows WHERE DOE BETWEEN '5/15/2020' AND '6/22/2020'")
    affectedm = len(monthly_affected)
    monthly_recovered = db.execute("SELECT id FROM shows WHERE DOR BETWEEN '5/15/2020' AND '6/22/2020'")
    recoveredm = len(monthly_recovered)
    monthly_death = db.execute("SELECT id FROM shows WHERE DOD BETWEEN '5/15/2020' AND '6/22/2020'")
    deathm = len(monthly_death)
    total_affected = db.execute("SELECT DOE FROM shows")
    affectedt = len(total_affected)
    total_recovered = db.execute("SELECT DOR FROM shows WHERE status = 0")
    recoveredt = len(total_recovered)
    total_death = db.execute("SELECT DOD FROM shows WHERE status = 2")
    deatht = len(total_death)
    return render_template("homepage.html", affected = affected, recovered = recovered, death = death, affectedw = affectedw, recoveredw = recoveredw,deathw = deathw, affectedm = affectedm,recoveredm = recoveredm,deathm = deathm, affectedt = affectedt,recoveredt = recoveredt,deatht = deatht)