from models import *



db.connect()
db.drop_tables([Userstory], safe=True)
db.create_tables([Userstory], safe=True)
