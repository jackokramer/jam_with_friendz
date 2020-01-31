from flask import Flask, session, render_template, request, redirect, flash
from mysqlConnect import connectToMySQL
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "burrito"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'
)

@app.route('/')
def index():
    mysql = connectToMySQL('jam')
    return render_template('login.html')

@app.route("/regis", methods=['POST'])
def regis():
    is_valid = True
    if not EMAIL_REGEX.match(request.form['email']):
        is_valid = False
        flash("please enter in a valid email")
    if request.form['password'] != request.form['c_password']:
        is_valid = False
        flash('passwords must match')
    if len(request.form['first_name']) < 1:
        is_valid = False
        flash("please use more than one character")
    if len(request.form['last_name']) < 1:
        is_valid = False
        flash("please use more than one character")
    if len(request.form['password']) < 8:
        is_valid = False
        flash("please use more than eight characters")
    if len(request.form['c_password']) < 8:
        is_valid = False
        flash("please use more than eight characters")
    if not is_valid:
        return redirect("/")
    else:
        mysql = connectToMySQL('jam')
        query = "INSERT INTO users(first_name, last_name, email, password, c_password, created_at, updated_at) VALUES(%(fn)s, %(ln)s, %(em)s, %(ps)s, %(cp)s, NOW(), NOW())"
        hashed_pw = bcrypt.generate_password_hash(request.form['password'])
        data ={
            'fn': request.form['first_name'],
            'ln': request.form['last_name'],
            'em': request.form['email'],
            'ps': hashed_pw,
            'cp': hashed_pw
        }
        validated = mysql.query_db(query, data)
        if validated:
            session['user_id'] = validated
        return redirect("/verif")

@app.route("/verif")
def verif():
    mysql =  connectToMySQL('jam')
    query = "SELECT first_name, last_name FROM users WHERE user_id =%(id)s"
    data = {
        'id': session['user_id']
    }
    results = mysql.query_db(query,data)
    if results:
        users = results[0]
    return render_template('verif.html', users=users)

@app.route("/finish", methods= ['POST'])
def finish():
    is_valid = True
    if len(request.form['college'])<1:
        is_valid = False
        flash("please do not leave the field blank")
    if len(request.form['city'])<1:
        is_valid = False
        flash("please do not leave the field blank")
    # HAVING difficulty on how to sort these verifications out.
    #if len(request.form['guitar'])
    #if len(request.form['bass'])
    #if len(request.form['trumpet'])
    #if len(request.form['violin'])
    #if len(request.form['drums'])
    if len(request.form['about'])<1 :
        is_valid = False
        flash("please fill in the bio section")
    if len(request.form['about'])>256 :
        is_valid = False
        flash("please limit the character count to 256 or less")
    else:
        mysql = connectToMySQL('jam')
        query =  "INSERT INTO extras(college, city, about) VALUES(%(cl)s, %(ci)s, %(ab)s)"
        data = {
            "cl": request.form['college'],
            "ci": request.form['city'],
            #"in": request.form['instruments'],
            "ab": request.form['about']
        }
        finished = mysql.query_db(query, data)
        if finished:
            session['user_id'] = finished
        return redirect("/homepage")

    

@app.route("/login", methods= ['POST'])
def login():
    is_valid = True
    if len(request.form['email'])<1:
        is_valid = False
        flash("email cannot be blank")
    #if len(request.form['password'])<1:
    mysql = connectToMySQL('jam')
    query = "SELECT user_id, email, password FROM users WHERE email = %(em)s AND user_id = %(ud)s"
    data = { 
        'em': request.form['email'],
        'ud': session['user_id']
    }
    logged = mysql.query_db(query, data)

    if logged:
        user = logged[0]
        if bcrypt.check_password_hash(user['password'], request.form['password']):
            session['user_id'] = user['user_id']
            return redirect('/homepage')
        else:
            is_valid = False
    else:
        is_valid = False
        flash('email doesnt exist')

    if not is_valid:
        flash('invalid password or email')
        return redirect("/homepage")

@app.route("/homepage")
def homepage():
    mysql = connectToMySQL('jam')
    query = "SELECT first_name, last_name FROM users WHERE user_id(%(id)s)"
    data = {
        'id': session['user_id'] 
    }
    homes = mysql.query_db(query, data)
    if homes:
        homes = homes[0]
    return render_template("index.html", users = homes)

@app.route("/signups")
def signups():
    mysql = connectToMySQL('jam')
    query = "SELECT first_name, last_name FROM users WHERE user_id(%(id)s)"
    data = {
        'id': session['user_id'] 
    }
    homes = mysql.query_db(query, data)
    if homes:
        homes = homes[0]
    return render_template("signus.html", homes=homes)
    
@app.route("/reherse", methods =['POST'])
def reherese():
    mysql = connectToMySQL('jam')
    query = "INSERT into spaces(')"
    return render_template('signus.html')

@app.route("/stores")
def stores():
    return render_template('stores.html')

@app.route("/concerts")
def concerts():
    return render_template("concerts.html")

@app.route("/sessions")
def upcoming():
    return render_template('logged_sess.html')

@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')



if "__main__" == __name__:
    app.run(debug=True, port=5001)
