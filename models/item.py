from db import db

class ItemModel(db.Model):

    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(80)) # 80 char limit
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self. price = price
        self.store_id = store_id

    def json(self):
        # returns representation of model as a json (dictionary)
        return {'name': self.name, 'price': self.price}
    
    @classmethod
    def find_by_name(cls, name):
        # query the item model, then filter it by name and first found
        return cls.query.filter_by(name=name).first() 

    def save_to_db(self):
        # session = collection of items being written to db
        db.session.add(self) 
        db.session.commit()

    def delete_from_db(self):
        # session = collection of items being written to db
        db.session.delete(self) 
        db.session.commit()
        