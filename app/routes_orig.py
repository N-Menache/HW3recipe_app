from app import myapp_obj
from flask import render_template
from flask import redirect
from flask import request
from app.forms import LoginForm
from app.models import User
from app.models import Favorites
from app import db

login_username = ""
login_password = ""

@myapp_obj.route("/")
def main():
    db.create_all()
    return "main"

@myapp_obj.route("/accounts")
def users():
    return "my USER ACCOUNTS"

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    global login_username
    global login_password
    form = LoginForm()
    if form.validate_on_submit():
        print(f"Here is the input from the user {form.username.data} and {form.password.data}")
        login_username = form.username.data
        login_password = form.password.data
        return redirect("/")
    else:
        print("MOOOO MOOO")
    return render_template("login.html", form=form)

@myapp_obj.route('/submit', methods=['GET', 'POST'])
def submit():
    # Get the user data
    name = request.form.get('name')
    password = request.form.get('password')
    email = request.form.get('email')
    movie = request.form.get('movie')
    user = User(username=name, password=password, email=email)
    db.session.add(user)
    user_id=User.query.order_by(User.id.desc()).first().id
    user = User.query.get(user_id)
    favorites = Favorites(movie=movie, user_id=user_id)
    db.session.add(favorites)
    db.session.commit()
    return render_template("submit.html")

@myapp_obj.route("/showall")
def showall():
    print(f"Name: {login_username}, Password: {login_password}")
    query = db.session.query(User).filter(User.username == login_username, User.password == login_password)
    if query.count() > 0:
         favorites = Favorites.query.all()
         return render_template('showall.html', favorites=favorites)
    else: 
         return "Username and password do not match"
