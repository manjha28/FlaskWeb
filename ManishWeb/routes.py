from ManishWeb import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from ManishWeb.models import Item,User
from ManishWeb.forms import RegisterForm,LoginForm
from ManishWeb import db

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/about/<username>')
def about_page(username):
    return f"<h4>The About page tells about {username}</h4>"





@app.route('/market')
def market_page():
    items = Item.query.all()
    # items = [
    #     {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    #     {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    #     {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    # ]
    return render_template('market.html', items=items)

'''Rote for register page which contains a form'''
@app.route('/register', methods = ['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email=form.email.data,
                              password_h=form.password1.data)

        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}: # If there's no error message in the dictionary
        for err_msg in form.errors.values():
            flash(f"The error is {err_msg}", category = 'danger') #danger is used in category because it has it's reference in Bootstrap classes
    return render_template('register.html',form = form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    return render_template('login.html', form=form)