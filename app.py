from flask import Flask, render_template, redirect, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import (
    Employee,
    Department,
    db,
    connect_db,
    get_directory,
    get_directory_join,
    get_directory_join_class,
)
from forms import AddSnackForm, EmployeeForm

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///employees_db"
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "abc123"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

connect_db(app)
app.app_context().push()


debug = DebugToolbarExtension(app)


@app.route("/")
def home_page():
    return render_template("home.html")


@app.route("/phones")
def list_phones():
    emps = Employee.query.all()

    return render_template("phones.html", emps=emps)


@app.route("/snacks/new", methods=["GET", "POST"])
def add_snack():
    """An add snack form"""

    form = AddSnackForm()

    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data

        flash(f"Created new snack: name is {name}. Price is ${price}")
        return redirect("/")
    else:
        return render_template("add_snack_form.html", form=form)


@app.route("/employees/new", methods=["GET", "POST"])
def add_employee():
    form = EmployeeForm()

    # depts = db.session.query(Department.dept_code, Department.dept_name)
    form.dept_code.choices = [
        (d.dept_code, d.dept_name) for d in Department.query.all()
    ]

    if form.validate_on_submit():
        name = form.name.data
        state = form.state.data
        dept_code = form.dept_code.data

        emp = Employee(name=name, state=state, dept_code=dept_code)
        db.session.add(emp)
        db.session.commit()

        return redirect("/phones")
    else:
        return render_template("add_employee_form.html", form=form)


@app.route("/employees/<int:id>/edit", methods=["GET", "POST"])
def edit_employee(id):
    """edit an employee's data"""
    emp = Employee.query.get_or_404(id)
    form = EmployeeForm(obj=emp)
    form.dept_code.choices = [
        (d.dept_code, d.dept_name) for d in Department.query.all()
    ]

    if form.validate_on_submit():
        emp.name = form.name.data
        emp.state = form.state.data
        emp.dept_code = form.dept_code.data
        db.session.commit()
        return redirect("/phones")

    else:
        return render_template("edit_employee_form.html", form=form)
