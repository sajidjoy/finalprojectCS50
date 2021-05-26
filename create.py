import cs50
import csv

open(f"corona_report.db", "w").close()
db = cs50.SQL("sqlite:///corona_report.db")

db.execute("CREATE TABLE shows (id NUMERIC,country TEXT,state TEXT,city TEXT,DOE DATE,DOR DATE,DOD DATE,status NUMERIC)")
