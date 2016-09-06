from peewee import *
import connect

db = PostgresqlDatabase(connect.database_name, user=connect.name)


class BaseModel(Model):

    class Meta:
        database = db


class Userstory(BaseModel):
    story_title = CharField()
    user_story = CharField()
    acceptance_criteria = CharField()
    business_value = FloatField()
    estimation = FloatField()
    status = CharField()
