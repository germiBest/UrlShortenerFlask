from app import db

association_table = db.Table('association', db.Model.metadata,
    db.Column('key', db.Integer, db.ForeignKey('api.key')),
    db.Column('short', db.Integer, db.ForeignKey('links.short'))
)

class Links(db.Model):
    __tablename__ = 'links'
    short = db.Column(db.String(3), primary_key = True)
    link = db.Column(db.String(2048), nullable=False)
    created = db.Column(db.Date, nullable=False)
    expired = db.Column(db.Date, nullable=False)


    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Api(db.Model):
    __tablename__ = 'api'
    key = db.Column(db.String(32), primary_key=True)
    links = db.relationship("Links", secondary=association_table)