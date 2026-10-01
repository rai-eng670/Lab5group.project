LAB 05 REFERENCE PROJECT

This is an AI-generated reference implementation, not a claim of student
or team authorship. The assignment's page 5 prohibits using AI to generate
complete submitted solutions. Use this example to understand the design
and follow your instructor's rules when writing your own work.

Run in PyCharm
1. Extract the zip and open the Lab05 folder as a project.
2. Select or create a Python interpreter for this project.
3. In the PyCharm terminal, run: python -m pip install -r requirements.txt
4. Run app.py, then open http://127.0.0.1:5000/ in your browser.
5. The same report is available at http://127.0.0.1:5000/payroll.
   If port 5000 is busy, use:
   python -m flask --app app run --debug --port 5001

PyCharm settings from the instructions
Rename the displayed project to:
Designing and Programming a Payroll System with Object-Oriented Principles
Keep the actual submission folder named Lab05. If using a Flask run
configuration, set app.py as the target and enable debug mode. Running
app.py directly already enables debug mode for local development.

Expected sample results
Invoice payments: 226.50 and 85.98
Secretary: 1000.00
Manager: 8500.00
Executive manager: 14500.00
Sales person: 1200.00
Employees: 4; invoices: 2; total gross: 25512.48

Design notes
Payable and Employee are abstract. Employee contains a Person object.
Each employee subclass reuses its parent's to_dict() method. Every item
is serialized through the same serialize_payroll() function.
The class counters track objects created during the Python process.
The report subtracts the starting counts to count this batch only.
This is a local, single-user classroom demonstration, not a production
payroll system. The SSNs are deliberately invalid fictional values.

Reflection and team work
reflection.docx contains concept answers and two clearly marked fields
for your real team responsibilities and personal challenge. Complete
those honestly. The PDF requires 2-3 students, fair contributions, names
in file headers, and at least two classes/files per member. It also asks
for all remaining classes in models.py; coordinate class-level ownership
with your team and instructor rather than inventing contributions.
Use your actual version-control history for collaborative work.

Packaging your own completed work
Include reflection.docx inside Lab05 and upload it separately as well.
Remove .idea, .venv, and __pycache__ before making Lab05.zip.
