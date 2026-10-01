# Author: ChatGPT (reference example for Rithik Saini)
# Date: 10/01/2026
# Name: app.py
# Description: Display the payroll report with Flask.
# AI acknowledgment: ChatGPT generated this reference code.

from flask import Flask, render_template
from payroll.payroll import build_payroll_data

app = Flask(__name__)


@app.route("/")
@app.route("/payroll")
def payroll():
    data = build_payroll_data()
    return render_template("payroll.html", **data)


if __name__ == "__main__":
    app.run(debug=True)
