import app
from app.models import Links

print(Links.query.filter_by(api_key='').all())
#app.db.delete
#delete = app.models.Links.query.filter(Links.expired < date.today()).delete()
#delete.execute()