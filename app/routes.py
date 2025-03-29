from app import myapp_obj
from flask import render_template
from flask import redirect
from flask import request
from flask import flash
from app.forms import LoginForm, RecipeForm, UserForm
from app.models import User, Recipe
from app import db

logged_in_user = None 

@myapp_obj.route("/")
def main():
    db.create_all()
    if (logged_in_user):    
        return f"User {logged_in_user.name} is currently logged in."
    else:
        return "No user is currently logged in."

@myapp_obj.route("/logout")
def logout():
    global logged_in_user
    if (logged_in_user):
        username = logged_in_user.name
        logged_in_user = None
        return f"User {username} has been logged out."
    else:
        return "No user is currently logged in."

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    global logged_in_user
    form = LoginForm()
    if form.validate_on_submit():
        query = db.session.query(User).filter(User.name == form.username.data, User.password == form.password.data)
        if query.count() > 0:
            logged_in_user = query.first()
            return f"User {form.username.data} is now logged in."
        else:
            query = db.session.query(User).filter(User.name == form.username.data)
            if query.count() > 0:
                flash('Invalid password.')
            else:
                flash('Unknown user.')
    else:
        print("Username field must have data abd Password must be 4 to 35 characters.")
    form.username.data = ""
    form.password.data = ""
    return render_template("login.html", form=form)

@myapp_obj.route('/adduser', methods=['GET', 'POST'])
def add_user():
    # Get the user data
    form = UserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')
            print ({name})
            print ({email})
            print ({password})
            query = db.session.query(User).filter(User.name == name, User.password == password)
            if query.count() == 0:
                user = User(name=name, email=email, password=password)
                db.session.add(user)
                db.session.commit()
                print ("User added.")
            else:
                print ("Username already exists.")
                flash("Username already exists.")
        else:
            print ("Not valid form.")
    return render_template("add_user.html",  form=form)

@myapp_obj.route("/showall")
def showall():
    #query = db.session.query(User).filter(User.username == login_username, User.password == login_password)
    #if query.count() > 0:
    #     favorites = Favorites.query.all()
    #     return render_template('showall.html', favorites=favorites)
    #else: 
    return "Username and password do not match"

@myapp_obj.route("/recipe/new", methods=['GET', 'POST'])
def recipe_new():
    if (logged_in_user) :
        form = RecipeForm()
        if form.validate_on_submit():
            title = request.form.get('title')
            description = request.form.get('description')
            ingredients = request.form.get('ingredients')
            instructions = request.form.get('instructions')
            form.title.data = ""
            form.description.data = ""
            form.ingredients.data = ""
            form.instructions.data = ""
            recipe = Recipe(title=title, description=description, ingredients=ingredients, instructions=instructions, username=logged_in_user.username)
            db.session.add(recipe)
            db.session.commit()
            flash('Form successfully submitted!')
            return render_template('recipe_new.html', form=form)
        else:
            form.title.data = ""
            form.description.data = ""
            form.ingredients.data = ""
            form.instructions.data = ""
            flash('Please fill in all required fields.', category='warning')
            return render_template('recipe_new.html', form=form)
    else:
        return ("This page requires a login.")
    
@myapp_obj.route("/or/recipes")
def recipe_list():
    if (logged_in_user) :
        recipe_list = Recipe.query.all()
        return render_template('recipe_list.html', recipe_list=recipe_list)
    else:
        return ("This page requires a login.")
        

@myapp_obj.route("/recipe/<int:id>")
def recipe_details(id):
    if (logged_in_user) :
        if ( db.session.query(Recipe).count() == 0 ):
            return ("No recipes found.")
        else:
            recipe = Recipe.query.get(id)
            if (recipe):
                return render_template('recipe_details.html', recipe=recipe)
            else:
                return f"Recipe number {id} not found."
    else:
        return ("This page requires a login.")
    
@myapp_obj.route("/recipe/<int:id>/delete")
def recipe_delete(id):
    if (logged_in_user) :
        if ( db.session.query(Recipe).count() == 0 ):
            return ("No recipes found.")
        else:
            recipe = Recipe.query.get(id)
            if (recipe):
                title = recipe.title
                db.session.delete(recipe)
                db.session.commit()
                return f"Recipe number {id}, {title}, has been deleted."
            else:
                return f"Recipe number {id} not found."
    else:
        return ("This page requires a login.")
