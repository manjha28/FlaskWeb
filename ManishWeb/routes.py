from ManishWeb import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages,request
from ManishWeb.models import Item,User
from ManishWeb.forms import RegisterForm,LoginForm, PurchaseItemForm, SellItemForm
from ManishWeb import db
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/about/<username>')
def about_page(username):
    return f"<h4>The About page tells about {username}</h4>"





@app.route('/market', methods=['GET','POST'])
@login_required
def market_page():
    purchase_form = PurchaseItemForm()
    selling_form = SellItemForm()
    if request.method == "POST":
        #Purchase Item Logic
        purchased_item = request.form.get('purchased_item')
        p_item_object = Item.query.filter_by(name=purchased_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.buy(current_user)
                flash(f"Congratulations! You purchased {p_item_object.name} for {p_item_object.price}$", category='success')
            else:
                flash(f"Unfortunately, you don't have enough money to purchase {p_item_object.name}!", category='danger')
        #Sell Item Logic
        sold_item = request.form.get('sold_item')
        s_item_object = Item.query.filter_by(name=sold_item).first()
        if s_item_object:
            if current_user.can_sell(s_item_object):
                s_item_object.sell(current_user)
                flash(f"Congratulations! You sold {s_item_object.name} back to market!", category='success')
            else:
                flash(f"Something went wrong with selling {s_item_object.name}", category='danger')


        return redirect(url_for('market_page'))

    if request.method == "GET":
        items = Item.query.filter_by(owner=None)
        owned_items = Item.query.filter_by(owner=current_user.id)
        return render_template('market.html', items=items, purchase_form=purchase_form, owned_items=owned_items, selling_form=selling_form)
# def market_page():
#     purchase_item = PurchaseItemForm()
#     ''' LOC below throws us a conirm form submission everytime I refreshed'''
#     # if purchase_item.validate_on_submit():
#     #     print(request.form.get('purchased_item'))
#     if request.method == 'POST':
#         purchased_item = request.form.get('purchased_item')
#         p_item_object = Item.query.filter_by(name=purchased_item).first()
#         if p_item_object:
#             if current_user.can_purchase(p_item_object):
#                 p_item_object.buy(current_user)
#
#                 flash(f"Congratulations! You have successfully purchased {p_item_object.name} for {p_item_object.price}", category='success')
#             else:
#                 flash(f"You do not have enough funds to purchase {p_item_object.name} as the remaining balance is {p_item_object.price}", category='danger')
#             return redirect(url_for('market_page'))
#     if request.method == 'GET':
#         items = Item.query.filter_by(owner=None)
#         owned_items = Item.query.filter_by(owner=current_user.id)
#         return render_template('market.html', items=items, purchase_item=purchase_item, owned_items=owned_items)
        # items = [
    #     {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    #     {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    #     {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    # ]


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
        login_user(user_to_create)
        flash(f'You have successfuly created your account! You are now logged in as {user_to_create.username}', category='success')
        return redirect(url_for('market_page'))
    if form.errors != {}: # If there's no error message in the dictionary
        for err_msg in form.errors.values():
            flash(f"The error is {err_msg}", category = 'danger') #danger is used in category because it has it's reference in Bootstrap classes
    return render_template('register.html',form = form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f"Sucessfuly Logged in as {attempted_user.username}", category='success')
            return redirect(url_for('home_page'))
        else:
            flash('Username or password does not match or incorrect! Please Try again', category='danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash(f"Successfully logged out!", category='info')
    return redirect(url_for('home_page'))
