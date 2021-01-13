from app import db
import random
from datetime import date, timedelta

CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

class Links(db.Model):
    __tablename__ = 'links'
    short = db.Column(db.String(4), primary_key = True)
    link = db.Column(db.String(2048), nullable=False)
    created = db.Column(db.Date, default=date.today(), nullable=False)
    expired = db.Column(db.Date, nullable=False)
    api_key = db.Column(db.String(32), db.ForeignKey('api.key'), nullable=True)

    def __init__(self, link, expired, api_key=None):
        super().__init__()
        self.link = link
        self.expired = date.today() + timedelta(days=expired)
        self.short = self.short_gen()
        self.api_key = api_key

    def short_gen(self):
        short = ''.join(random.choices(CHARS, k=4))
        
        if not self.query.filter_by(short=short):
            return self.short_gen()
        return short

class Api(db.Model):
    __tablename__ = 'api'
    key = db.Column(db.String(32), primary_key=True)
    links = db.relationship("Links", backref='api', lazy=True)
    
    def __init__(self):
        super().__init__()
        self.key = self.key_gen()
    
    def key_gen(self):
        key = ''.join(random.choices(CHARS, k=32))

        if not self.query.filter_by(key=key):
            return self.key_gen()
        return key
        
