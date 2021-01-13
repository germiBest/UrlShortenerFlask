from app import app, db, api
from app.models import Links, Api
from flask_restful import Resource, reqparse
import re
import datetime
from time import mktime
import json

parser = reqparse.RequestParser()
parser.add_argument('link', type=str, required=True)
parser.add_argument('expired', type=int)

class ShortLink(Resource):
    def get(self, key):
        lks = []
        for link in Links.query.filter_by(api_key=key).all():
            lks.append({"short": link.short,
                        "expired": mktime(link.expired.timetuple())})
        return {key: lks}
    def post(self, key):
        args = parser.parse_args()
        link = str(args['link'])
        if not Api.query.filter_by(key=key).first():
            return {"error": "wrong_api"}
        if not 1 <= int(args['expired']) <= 365:
            return {"error": "wrong_expired" }
        if args['expired']:
            expired = int(args['expired'])
        else:
            expired = 90
        if not re.match( r"(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[-a-z0-9]{2,63}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)", link):
            return {"error": "wrong_link" }
        link = Links(link = link, expired = expired, api_key=key)
        db.session.add(link)
        db.session.commit()
        return  {"short": link.short,
                "expired": mktime(link.expired.timetuple())}

api.add_resource(ShortLink, '/api/v1/<string:key>')
