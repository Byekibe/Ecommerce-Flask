from flask import render_template, request, url_for, redirect, session, flash

from store import app, db, bcrypt
from .forms import RegistrationForm
from .models import User

@app.route("/")
def home():
	return render_template("admin/index.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password=bcrypt.generate_password_hash(form.password.data)
        user=User(name=form.name.data, username=form.username.data, email=form.email.data, password=hash_password)
        db.session.add(user)
        # user = User(form.username.data, form.email.data, form.password.data)
        # db_session.add(user)
        flash(f'Thanks for registering', 'success')
        return redirect(url_for('home'))
    return render_template('admin/register.html', form=form)
