from ManishWeb import db
from ManishWeb import bcrypt
'''db.drop_all(),db.create_all(),item1 = Item.query.filter_by(name = 'Iphone 10'),i = Item.query.filter_by(name='Iphone').first().id,
'''
#TODO : Need to Learn About Flask Forms
#FIXME : I need to fix the Relationship b/w the User and Item

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    @property
    def password_h(self):
        return self.password

    @password_h.setter
    def password_h(self, plain_password):
        self.password = bcrypt.generate_password_hash(plain_password).decode('utf-8')


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
    def __repr__(self):
        return f'Item {self.name}'