from config import db
from models import User, Instrument, Genre, Post, Rehearsal_space, Jam_session
from flask import render_template, request, redirect, session, flash
import re



def index():
    return render_template('login.html')

def regis():
    is_valid = User.reg_validate(request.form)
    if not is_valid:
        return redirect("/")
    else:
        user = User.add_new_user(request.form)
        session['user_id'] = user.id
        return redirect("/verif")

def verif():
    user = User.current_user(session['user_id'])
    instruments = Instrument.get_list()
    return render_template('verif.html', user=user, instruments=instruments)

def finish():
    user = User.current_user(session['user_id'])
    if user.profile_validate(request.form):
        user.profile_update(request.form)
        return redirect("/homepage")
    return redirect('/verif')

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

def stores():
    return render_template('stores.html')

def concerts():
    return render_template("concerts.html")

def upcoming():
    return render_template('logged_sess.html')

def logout():
    session.clear()
    return redirect('/')