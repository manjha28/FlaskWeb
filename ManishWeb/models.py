from ManishWeb import db


class Item(db.Model):
    #Don't know the reason why the reference cannot be find
    id = db.Column(db.Integer(),primary_key = True)
    name = db.Column(db.String(length = 30),nullable = False,unique = True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=14), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    #A magic method which returns the variable we want instead of default options
    def __repr__(self):
        return f'Item {self.name}'