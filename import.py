import csv
import cs50

con = cs50.SQL("sqlite:///corona_report.db")

with open('corona_reports.csv','r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        person = (row["id"])
        country = (row["country"])
        state = (row["state"])
        city = (row["city"])
        doe = (row["date of effected"])
        dor = (row["date of recovered"])
        dod = (row["dete of death"])
        status = (row["status"])

        con.execute("INSERT INTO shows (id,country,state,city,DOE,DOR,DOD,status) VALUES(?,?,?,?,?,?,?,?)",
                    person,country,state,city,doe,dor,dod,status)