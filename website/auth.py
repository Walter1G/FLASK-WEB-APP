from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be atleast 4 characters', category='error')
        elif len(firstName) < 2:
            flash('first name must be greater than 2 characters', category='error')
        elif len(password1) < 7:
            flash('Password must be longer than 7 characters', category='error')
        elif password1 != password2:
            flash('passwords must match', category='error')
        else:
            # add to db
            new_user = User(email=email, first_name=firstName, password=generate_password_hash(
                password1))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template('sign_up.html')
