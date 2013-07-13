import sqlite3

DB = None
CONN = None

import inspect

class User(object):
    def __init__(self, email, password, id, posts):
        self.email = email
        self.password = password
        self.id = id
        self.posts = posts

class Post(object):
    def __init__(self, title, body, user_id):
        self.title = title
        self.body = body
        self.user_id = user_id


#Connet to the super awesome database!
def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("upvote.db")
    DB = CONN.cursor()

# log in a user; they'll end up at a page with their email address displayed
# Links to: view your own posts, view others' posts, write a post.
def login_user(email):
    query = """SELECT * FROM users WHERE email = ?"""
    DB.execute(query, (email,))
    row = DB.fetchone()
    user = User(row[1], row[2], row[0], None)
    return user


# view your own posts: displays page with all posts by this tokened user
def get_posts(email):
    query = """SELECT posts.title, posts.body FROM posts INNER JOIN users ON posts.user_id = users.id Where users.email = ?"""
    DB.execute(query, (email,))
    rows = DB.fetchall()
    print "email is %r" %email
    return rows

# write a post page: needs to insert a new post into the posts table.

# view posts by others: needs to retrieve all posts written by users other than
# the logged in user and display them on a page, along with forms to submit votes.


# submit vote: needs to insert a new vote into the Votes table.
