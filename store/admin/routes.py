from flask import render_template, request, url_for, redirect, session, flash

from store import app, db
from .forms import RegistrationForm

@app.route("/")
def home():
	return render_template("layout.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        # user = User(form.username.data, form.email.data, form.password.data)
        # db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('admin/register.html', form=form)
