from db import db

class StoreModel(db.Model):

    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(80)) # 80 char limit

    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        # returns representation of model as a json (dictionary)
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}
    
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
        