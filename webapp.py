from flask import Flask, render_template, request
import hackbright_app

app = Flask(__name__)

@app.route("/")

def get_github():
    return render_template("get_github.html")

@app.route("/project")
def show_project_grades():
    hackbright_app.connect_to_db()
    project_name = request.args.get("project_name")
    rows = hackbright_app.show_grades_by_project(project_name)
    html = render_template("project_info.html", rows = rows,
                                                project = project_name)
    print project_name, rows, "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    return html

@app.route("/student")
def get_student():
    hackbright_app.connect_to_db()
    student_github = request.args.get("github")
    rows = hackbright_app.show_grades(student_github)
    html =  render_template("student_info.html", rows = rows,
                                         last_name = rows[0][1],
                                         first_name = rows[0][0])  

    return html

@app.route("/new_student")
def make_new_student():
    hackbright_app.connect_to_db()
    first_name = request.args.get("first_name")
    last_name = request.args.get("last_name")
    github = request.args.get("github")
    #the for label in add_student.html aligns with the above variables.
    success_message = hackbright_app.make_new_student(first_name, last_name, github)
    html = render_template("new_student.html", message = success_message)
    return html

@app.route("/add_student")
def add_student():
    return render_template("add_student.html")

@app.route("/new_project")
def make_new_project():
    hackbright_app.connect_to_db()
    project_name = request.args.get("project")
    description = request.args.get("description")
    max_grade = request.args.get("max_grade")
    success_message = hackbright_app.make_new_project(project_name, description, max_grade)
    html = render_template("new_project.html", message = success_message)
    return html

@app.route("/add_project")
def add_project():
    return render_template("add_project.html")

@app.route("/add_grade")
def add_grade():
    return render_template("add_grade.html")

@app.route("/grade_added")
def grade_added():
    hackbright_app.connect_to_db()
    github = request.args.get("github")
    project = request.args.get("project")
    grade = request.args.get("grade")
    success_message = hackbright_app.make_grade_for_student(github, project, grade)
    html = render_template("grade_added.html", message = success_message)
    return html


if __name__ == "__main__":
    app.run(debug = True)
