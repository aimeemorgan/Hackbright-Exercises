from flask import Flask, render_template, request
import hackbright_app

app = Flask(__name__)

@app.route("/")

def get_github():
    return render_template("get_github.html")

@app.route("/project")
def show_project_grades():
    hackbright_app.connect_to_db()
    project_name = request.args.get("project")
    rows = hackbright_app.show_grades_by_project(project_name)
    #html = render_template("project_grades.html" rows = rows,
         #                                        project = rows[0][2])
    print rows, "THIS IS WHAT YOU WANTED!!!!!!!!!!!!!!!!!!!!!^#&^#$%#@"
    return "!!!!!!!!!!!!!!!!!!!!!"

@app.route("/student")
def get_student():
    hackbright_app.connect_to_db()
    student_github = request.args.get("github")
    rows = hackbright_app.show_grades(student_github)
    html = render_template("student_info.html", rows = rows,
                                                last_name = rows[0][1],
                                                first_name = rows[0][0])  
   


    

    return html


if __name__ == "__main__":
    app.run(debug = True)