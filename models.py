from flask import session, flash
from config import db, bcrypt
from sqlalchemy.sql import func, or_
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

user_instruments = db.Table(
    'user_instruments',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='cascade'), primary_key=True),
    db.Column('instrument_id', db.Integer, db.ForeignKey('instrument.id', ondelete='cascade'), primary_key=True),
)

attendance = db.Table(
    'attendance',
    db.Column('attendee', db.Integer, db.ForeignKey('user.id', ondelete='cascade'), primary_key=True),
    db.Column('session_id', db.Integer, db.ForeignKey('jam_session.id', ondelete='cascade'), primary_key=True)
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    college = db.Column(db.String(255))
    city = db.Column(db.String(255))
    about = db.Column(db.Text)
    major = db.Column(db.String(255))
    instruments = db.relationship('Instrument', secondary=user_instruments)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    genre = db.relationship('Genre', foreign_keys=[genre_id], backref='users')
    proficiency = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    def profile_validate(self, form):
        is_valid = True
        if len(form['college'])<1:
            is_valid = False
            flash("please do not leave the field blank")
        if len(form['city'])<1:
            is_valid = False
            flash("please do not leave the field blank")
        # HAVING difficulty on how to sort these verifications out.
        #if len(form['guitar'])
        #if len(form['bass'])
        #if len(form['trumpet'])
        #if len(form['violin'])
        #if len(form['drums'])
        if len(form['about'])<1 :
            is_valid = False
            flash("please fill in the bio section")
        if len(form['about'])>256 :
            is_valid = False
            flash("please limit the character count to 256 or less")
        return is_valid
    def profile_update(self, form):
        self.college = form['college']
        self.city = form['city']
        for inst_id in form.getlist('instruments'):
            instrument = Instrument.query.get(inst_id)
            self.instruments.append(instrument)
        self.genre = form['genre']
        self.about = form['about']
        db.session.commit()
    
    @classmethod
    def reg_validate(cls, form):
        is_valid = True
        if not EMAIL_REGEX.match(form['email']):
            is_valid = False
            flash("please enter in a valid email")
        if form['password'] != form['c_password']:
            is_valid = False
            flash('passwords must match')
        if len(form['first_name']) < 1:
            is_valid = False
            flash("please use more than one character")
        if len(form['last_name']) < 1:
            is_valid = False
            flash("please use more than one character")
        if len(form['password']) < 8:
            is_valid = False
            flash("please use more than eight characters")
        if len(form['c_password']) < 8:
            is_valid = False
            flash("please use more than eight characters")
        return is_valid
    @classmethod
    def add_new_user(cls, form):
        pw_hash = bcrypt.generate_password_hash(form['password'])
        new_user = cls(
            first_name = form['first_name'],
            last_name = form['last_name'],
            email = form['email'],
            password = pw_hash
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user
    @classmethod
    def log_validate(cls, form):
        user = cls.query.filter_by(email=form['email']).all()
        if not user:
            flash('email doesnt exist', 'log_un')
        elif not bcrypt.check_password_hash(user[0].password, form['password']):
            flash('invalid password or email', 'log_pw')
        if '_flashes' in session.keys():
            return False
        return user[0]
    @classmethod
    def current_user(cls, id):
        user = cls.query.get(id)
        return user
    @classmethod
    def username_check(cls, form):
        names = cls.query.filter_by(username=form['un']).all()
        if names:
            return True
        return False

class Instrument(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    users = db.relationship('User', secondary=user_instruments)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    @classmethod
    def get_list(cls):
        instruments = cls.query.all()
        return instruments

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    @classmethod
    def get_list(cls):
        genre = cls.query.all()
        return genre

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

class Rehearsal_space(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='cascade'), nullable=False)
    user = db.relationship('User', foreign_keys=[user_id], backref='spaces')
    # available dates
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

class Jam_session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    space_id = db.Column(db.Integer, db.ForeignKey('rehearsal_space.id', ondelete='cascade'), nullable=False)
    space = db.relationship('Rehearsal_space', foreign_keys=[space_id], backref='sessions')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='cascade'), nullable=False)
    host = db.relationship('User', foreign_keys=[user_id], backref='sessions')
    attendance_limit = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())