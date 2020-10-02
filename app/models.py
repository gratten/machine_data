from app import db

class Machine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project = db.Column(db.String(8), index=True)
    serialnum = db.Column(db.String(64), index=True, unique=True)
    customer = db.Column(db.String(64))
    description = db.Column(db.String(128))
    kits = db.relationship('Kit', backref='parent', lazy='dynamic')

    def __repr__(self):
        return f'<Machine {self.serialnum}>'

class Kit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project = db.Column(db.String(8), index=True)
    serialnum = db.Column(db.Integer, db.ForeignKey('machine.serialnum'))
    customer = db.Column(db.String(64))
    speed = db.Column(db.Integer)
    length = db.Column(db.Float)
    width = db.Column(db.Float)
    depth = db.Column(db.Float)

    def __repr__(self):
        return f'<Kit {self.length}x{self.width}x{self.depth}>'