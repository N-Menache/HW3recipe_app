#  This file defines the routes for the Recipe application

from app import myapp_obj
from flask import render_template
from flask import redirect
from flask import request
from flask import flash
from app.forms import LoginForm, RecipeForm, UserForm
from app.models import User, Recipe
from app import db

# This global variable idicates who is logged in currently. None indicates no one is logged in.
logged_in_user = None 

# This route is for main page. Displays which user is currently logged in.
@myapp_obj.route("/")
def main():
    db.create_all()
    if (logged_in_user):    
        return f"User {logged_in_user.name} is currently logged in."
    else:
        return "No user is currently logged in."

# This route is used to logout the current user
@myapp_obj.route("/logout")
def logout():
    global logged_in_user
    # If there is a user currently logged in, they are logged out.
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
    # Check for POST method submitting form
    if request.method == 'POST':
        if form.validate_on_submit():
            # If the login information is valid, find the user in the User table based on user name and password
            query = db.session.query(User).filter(User.name == form.username.data, User.password == form.password.data)
            # If the user logging in was found in the User table, login the user
            if query.count() > 0:
                logged_in_user = query.first()
                return f"User {form.username.data} is now logged in."
            # Otherwise display message if the user is not found or an invalid password
            else:
                query = db.session.query(User).filter(User.name == form.username.data)
                if query.count() > 0:
                    flash('Invalid password.')
                else:
                    flash('Unknown user.')
        else:
            flash("All fields are required.")
    return render_template("login.html", form=form)

@myapp_obj.route('/adduser', methods=['GET', 'POST'])
def add_user():
    # Get the user data
    form = UserForm()
    # Check for POST method submitting form
    if request.method == 'POST':
        if form.validate_on_submit():
             # If the Add User information is valid, see if user is already the User table based in user name and password
            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')
            query = db.session.query(User).filter(User.name == name, User.password == password)
            # If the user has not been found in the User table, add them
            if query.count() == 0:
                user = User(name=name, email=email, password=password)
                db.session.add(user)
                db.session.commit()
                flash("User sucessfully added.")
            else:
                flash("Username already exists.")
        else:
            flash("All fields are required.")
    return render_template("add_user.html",  form=form)

@myapp_obj.route("/recipe/new", methods=['GET', 'POST'])
def recipe_new():
    if (logged_in_user) :
        form = RecipeForm()
        # Check for POST method submitting form
        if request.method == 'POST':
            if form.validate_on_submit():
                # If the recipe information is valid, add the Recipe to the Recipe table
                title = request.form.get('title')
                description = request.form.get('description')
                ingredients = request.form.get('ingredients')
                instructions = request.form.get('instructions')
                recipe = Recipe(title=title, description=description, ingredients=ingredients, instructions=instructions, username=logged_in_user.name)
                db.session.add(recipe)
                db.session.commit()
                flash('Form successfully submitted!')
            else:
                # Otherwise indicate to user to fill in required fields correctly
                flash('Please fill in all required fields.', category='warning')
        return render_template('recipe_new.html', form=form)
    else:
        return ("This page requires a login.")
    
@myapp_obj.route("/or/recipes")
def recipe_list():
    # If there is no user logged in, restrict access to this page
    if (logged_in_user) :
        # Query the recipe list  and send to the html template to display the recipe titles
        recipe_list = Recipe.query.all()
        return render_template('recipe_list.html', recipe_list=recipe_list)
    else:
        return ("This page requires a login.")
        

@myapp_obj.route("/recipe/<int:id>")
def recipe_details(id):
    # If there is no user logged in, restrict access to this page
    if (logged_in_user) :
        # Display the detailed recipe imformation if recipe number exists
        # Alert user if no recipes found or recipe number not found
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
    # If there is no user logged in, restrict access to this page
    if (logged_in_user) :
        # Delete specified if recipe number exists
        # Alert user if no recipes found or recipe number not found
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
