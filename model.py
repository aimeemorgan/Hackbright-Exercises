from flask import Flask, render_template, request
import app

my_app = Flask(__name__)

@my_app.route("/")
def landing_page():
    return render_template("upvote.html")

@my_app.route("/main_page")
def make_main():
    app.connect_to_db()
    email_addy = request.args.get("email")
    current_user = app.login_user(email_addy)
    html = render_template("main_page.html", user=current_user)
    return html

@my_app.route("/your_posts")
def your_posts():
    app.connect_to_db()
    email_addy = request.args.get("email")
    posts = app.get_posts(email_addy)
    html = render_template("my_posts.html", email=email_addy, rows=posts)
    return html


if __name__ == "__main__":
    my_app.run(debug = True)


