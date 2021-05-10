from ManishWeb import app
from flask import render_template
from ManishWeb.models import Item

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
