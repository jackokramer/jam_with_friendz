from config import db
from models import User, Instrument, Genre, Jam_session
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
    genre = Genre.get_list()
    return render_template('verif.html', user=user, instruments=instruments, genres=genre)

def finish():
    user = User.current_user(session['user_id'])
    if user.profile_validate(request.form):
        user.profile_update(request.form)
        return redirect("/homepage")
    return redirect('/verif')

def login():
    user = User.log_validate(request.form)
    if not user:
        return redirect('/')
    session['user_id'] = user.id
    return redirect("/homepage")

def homepage():
    homes = User.current_user(session['user_id'])
    return render_template("index.html", users = homes)

def profile(id):
    current_user = User.current_user(session['user_id'])
    user = User.current_user(id)
    instruments = ""
    for instrument in user.instruments:
        instruments += f"{instrument.name}, "
    instruments = instruments[:len(instruments)-2]
    return render_template("profile.html", current_user = current_user, user = user, instruments = instruments)

def signups():
    user = User.current_user(session['user_id'])
    return render_template("signus.html", homes=user)
    
def rehearse():
    is_valid = Jam_session.jam_validate(request.form)
    if not is_valid:
        return redirect('/signups')
    session = Jam_session.add_new_session(request.form)
    return redirect('/validated')

def validate():
    user = User.current_user(session['user_id'])
    return render_template('validate.html', user=user)

def cancel(id):
    pass

def stores():
    return render_template('stores.html')

def concerts():
    return render_template("concerts.html")

def upcoming():
    return render_template('logged_sess.html')

def logout():
    session.clear()
    return redirect('/')