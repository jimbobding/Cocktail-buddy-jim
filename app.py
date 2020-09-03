import os
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash


if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)


# ---- Collection Variables ----- #

drinks_db = mongo.db.drinks
users_db = mongo.db.users
alcohol_db = mongo.db.alcohol
alcohol_measurements_db = mongo.db.alcohol_measurements
alcohol_measurements_2_db = mongo.db.alcohol_measurements_2
citrus_db = mongo.db.citrus
citrus_measurements_db = mongo.db.citrus_measurements
sweet_measurements_db = mongo.db.sweet_measurements
glassware_db = mongo.db.glassware

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/cocktail_recipe/<drink_id>')
def cocktail_recipe(drink_id):
    created_by = session['user']
    selected_cocktail = drinks_db.find_one({"_id": ObjectId(drink_id)})
   
    return render_template("cocktail_recipe.html",
                           selected_cocktail=selected_cocktail, created_by=created_by
                           )


@app.route('/drinks')
def drinks_card():
    drinks = list(drinks_db.find())
    return render_template("drinks.html", drinks=drinks)


@app.route('/show_categories/<name>')
def show_categories(name):
    drinks = list(drinks_db.find({'alcohol_type': name}))
    return render_template('my_bar.html',
                           drinks=drinks,
                           name=name)


# ---------- Calls Spirit Selection ----------- #
@app.route('/spirit_selection')
def spirit_selection():
    selected_alcohol = drinks_db.find_one('alcohol_type')
    drinks = mongo.db.drinks.find()
    return render_template("spirit_selection.html",
                           drinks=drinks, selected_alcohol=selected_alcohol)


# ---------- Add Cocktail  ----------- #
@app.route('/add_cocktails', methods=['GET', 'POST'])
def add_cocktails():
    if request.method == 'POST':

        # Dict with fields for new cocktail
        new_cocktail = {
            'alcohol_type': request.form.get('alcohol_type'),
            'drink_name': request.form.get('drink_name'),
            'alcohol_element': request.form.get('alcohol_element'),
            'alcohol_measure': request.form.get('alcohol_measure'),
            'citrus_element': request.form.get('citrus_element'),
            'citrus_measure': request.form.get('citrus_measure'),
            'sweet_element': request.form.get('sweet_element'),
            'sweet_measure': request.form.get('sweet_measure'),
            'garnish': request.form.get('garnish'),
            'glass_type': request.form.get('glass_type'),
            'method': request.form.get('method'),
            'notes': request.form.get('notes'),
            'history': request.form.get('history'),
            'image': request.form.get('image'),
            'created_by': session['user']

        }
        drinks_db.insert_one(new_cocktail)
        flash("Drink has been successfully created")
        return redirect(url_for("drinks_card"))

    alcohol = alcohol_db.find()
    alcohol_measurements = alcohol_measurements_db.find()
    alcohol_measurements_2 = alcohol_measurements_2_db.find()
    citrus_measurements = citrus_measurements_db.find()
    citrus_type = citrus_db.find()
    sweet_measurements = sweet_measurements_db.find()
    glassware = glassware_db.find()
    return render_template("add_cocktails.html",
                           alcohol=alcohol, alcohol_measurements=alcohol_measurements,
                            alcohol_measurements_2=alcohol_measurements_2, 
                            citrus_type=citrus_type, citrus_measurements=citrus_measurements,
                            sweet_measurements=sweet_measurements, glassware=glassware
                              )


# ---------- Edit Cocktail----------- #
@app.route('/edit_cocktail/<drink_id>', methods=['GET', 'POST'])
def edit_cocktail(drink_id):
    if request.method == 'POST':

        edit_cocktail = {
            'alcohol_type': request.form.get('alcohol_type'),
            'drink_name': request.form.get('drink_name'),
            'alcohol_element': request.form.get('alcohol_element'),
            'alcohol_measure': request.form.get('alcohol_measure'),
            'alcohol_element_2': request.form.get('alcohol_element_2'),
            'alcohol_measure_2': request.form.get('alcohol_measure_2'),
            'citrus_element': request.form.get('citrus_element'),
            'citrus_measure': request.form.get('citrus_measure'),
            'sweet_element': request.form.get('sweet_element'),
            'sweet_measure': request.form.get('sweet_measure'),
            'garnish': request.form.get('garnish'),
            'glass_type': request.form.get('glass_type'),
            'method': request.form.get('method'),
            'notes': request.form.get('notes'),
            'history': request.form.get('history'),
            'image': request.form.get('image'),
            'created_by': session['user']

        }
        drinks_db.update({"_id": ObjectId(drink_id)}, edit_cocktail)
        flash("Drink has been successfully edited")

    selected_cocktail = drinks_db.find_one({"_id": ObjectId(drink_id)})
    alcohol = alcohol_db.find()
    alcohol_measurements = alcohol_measurements_db.find()
    alcohol_measurements_2 = alcohol_measurements_2_db.find()
    citrus_measurements = citrus_measurements_db.find()
    citrus_type = citrus_db.find()
    sweet_measurements = sweet_measurements_db.find()
    glassware = glassware_db.find()
    return render_template("edit_cocktail.html",
                           alcohol=alcohol, alcohol_measurements=alcohol_measurements,
                            alcohol_measurements_2=alcohol_measurements_2, 
                            citrus_type=citrus_type,citrus_measurements=citrus_measurements,
                            sweet_measurements=sweet_measurements, glassware=glassware,
                            selected_cocktail=selected_cocktail)


# ---------- Delete Cocktail ----------- #
@app.route('/delete_cocktail/<drink_id>')
def delete_cocktail(drink_id):
    drinks_db.remove({"_id": ObjectId(drink_id)})
    flash("Your cocktail has been deleted")
    return redirect(url_for("drinks_card"))


# ---------- Get Categories----------- #
@app.route('/get_categories')
def get_categories():
    alcohol = list(alcohol_db.find().sort("alcohol_type", 1))
    return render_template("categories.html", alcohol=alcohol)


# ---------- Search/indexing ----------- #
@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form.get("query")
    drinks = list(drinks_db.find({"$text": {"$search": query}}))
    return render_template("drinks.html", drinks=drinks)


# ---------- Add Categories----------- #
@app.route('/add_categories', methods=['GET', 'POST'])
def add_categories():
    if request.method == "POST":
        alcohol = {
            "alcohol_type": request.form.get("alcohol_type")
        }
        alcohol_db.insert_one(alcohol)
        flash("New alcohol added")
        return redirect(url_for("get_categories"))

    return render_template("add_categories.html")


# ---------- Edit Categories----------- #
@app.route('/edit_categories/<alc_id>', methods=['GET', 'POST'])
def edit_categories(alc_id):
    if request.method == "POST":
        submit = {
            "alcohol_type": request.form.get("alcohol_type")
                 }
        alcohol_db.update({"_id": ObjectId(alc_id)}, submit)
        flash("category Updated")
        return redirect(url_for("get_categories"))
    alc = alcohol_db.find_one({"_id": ObjectId(alc_id)})
    return render_template("edit_categories.html", alc=alc)


# ---------- Dlete Categories----------- #
@app.route('/delete_categories/<alc_id>')
def delete_categories(alc_id):
    alcohol_db.remove({"_id": ObjectId(alc_id)})
    flash("category successfully deleted")
    return redirect(url_for("get_categories"))


# ---------- Register----------- #
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        # check if username exists in database
        existing_user = users_db.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Sorry username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password").lower())
        }

        users_db.insert_one(register)

        # put user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Succesfull")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# ---------- Login ----------- #
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        # check if username exists in database
        existing_user = users_db.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))

            else:
                # invalid match
                flash("Incorect password and/or username")
                return redirect(url_for("login"))

        else:
            flash("Incorect password and/or username")
            return redirect(url_for("login"))

    return render_template("login.html")


# ---------- Profile ----------- #
@app.route("/profile/<username>", methods=['GET', 'POST'])
def profile(username):
    # gets session username from the database
    drink = drinks_db.find()
    username = users_db.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username, drink=drink)

    return redirect(url_for("login"))


# ---------- Logout ----------- #
@app.route('/logout')
def logout():
    # Remove user session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
