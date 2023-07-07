from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


# Models go here:


class Department(db.Model):
    """Department: A department has many employees"""

    __tablename__ = "departments"

    dept_code = db.Column(db.Text, primary_key=True)
    dept_name = db.Column(db.Text, nullable=False, unique=True)
    phone = db.Column(db.Text)

    def __repr__(self):
        return f"<Department {self.dept_code} {self.dept_name} {self.phone}>"


class Employee(db.Model):
    """employees"""

    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    state = db.Column(db.Text, nullable=False, default="CA")
    dept_code = db.Column(db.Text, db.ForeignKey("departments.dept_code"))

    dept = db.relationship("Department", backref="employees")

    def __repr__(self):
        return f"<Employee {self.name} {self.state} {self.dept_code}>"


def get_directory():
    """Show phone directory"""

    all_emps = Employee.query.all()

    for emp in all_emps:
        if emp.dept is not None:
            print(emp.name, emp.dept.dept_name, emp.dept.phone)
        else:
            print(emp.name, "-", "-")


def get_directory_join():
    directory = (
        db.session.query(Employee.name, Department.dept_name, Department.phone)
        .join(Department)
        .all()
    )

    for name, dept, phone in directory:
        print(name, dept, phone)


def get_directory_join_class():
    directory = db.session.query(Employee, Department).join(Department).all()

    for emp, dept in directory:
        print(emp.name, dept.dept_name, dept.phone)
