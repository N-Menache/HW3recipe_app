# HW3recipe_app Read Me

This is a web application that allows users to create view, update and delete food recipes.

## Table of Contents

1. [Project Description](#project-description)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)

---

## Project Description
# The application includes the following pages:

- **/adduser**
New users navigate to this page first to add their username, email, and password. All fields are required.

- **/login**
Users login with their username and password added in the /adduser page. All fields are required.
Users cannot login if another user is already logged in.

- **/logout**
Currently logged in user is logged out by going to this page.

- **/**
Shows the name of the user currently logged in.

- **/or/recipes**
This page with an unordered list will show all of the names of the recipes you have.

- **/recipe/new**
This page will contain a form that will allow you to add a new recipe, including the title, description, ingredients, and instructions.

- **/recipe/<integer>**
This page will return one recipe with the details provided in the /recipe/new page along with the recipe author and date and time created. The <integer> field represents the recipe number.

- **/recipe/<integer>/delete**
This page will delete the specific recipe. The <integer> field represents the recipe number

---

## Features

- **User Authentication**: Allows adding of users and log in
- **Recipe Management**: Users can add and delete recipes, view a list of recipes and detailed information on each one.

---

## Installation

### Prerequisites

Ensure you have the following installed:

- [Git](https://git-scm.com/)
- [Python 3](https://www.python.org/downloads/) (if the project involves Python)
- Virtual environment venv
- libraries listed in requirements.txt

### Steps to Install

1. Clone the repository
   git clone -b master https://github.com/N-Menache/HW3recipe_app.git

2. Navigate to the project folder
   cd HW3recipe_app

3. **Install dependencies**:
   - For Python (backend dependencies):
     ```
     pip install -r requirements.txt
     ```

4. **Set up virtual environment**:
     ```
   - Use python3 -m venv venv to create the virtual environment and use source venv/bin/activate to initiate it
     ```
---

## Usage

### Running the Application

After installation, Navigate to app folder under HW3recipe_app
then run the application with the following command:

```
python3 run.py
```

This will start the development server, and you can access the app in your browser by clicking on the link generated in the terminal (E.g. `http://localhost:5000`). This will bring you to the main page. From there you can append the webpages described in the Project Description.
