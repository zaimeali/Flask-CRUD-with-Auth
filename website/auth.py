from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from flask_login import login_user, logout_user, login_required, current_user

auth = Blueprint('auth', __name__)


@auth.route('/check')
def check():
    return render_template("check.html", text="testing", user="zaime", boolean=True, fruit="banana")


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                flash('Logged In Successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.index'))
            else:
                flash('Incorrect Password', category='error')
        else:
            flash('User does not exist', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        if len(name) < 5:
            flash('Username should be greater than 2', category="error")
        else:
            new_user = User(email=email, name=name, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash('Your account has been created', category="success")
            login_user(new_user, remember=True)
            return redirect(url_for('views.index'))

    return render_template("register.html", user=current_user)
