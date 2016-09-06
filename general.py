from flask import Flask, redirect, url_for, render_template, request
from peewee import *


DATABASE = 'homework.db'
DEBUG = True



app = Flask(__name__)
app.config.from_object(__name__)
db = SqliteDatabase(DATABASE)


class UserStory(Model):
    story_title = CharField()
    user_story = TextField()
    criteria = TextField()
    b_value = IntegerField()
    estimation = FloatField()
    status = CharField()

    class Meta:
        database = db


def create_tables():
    db.connect()
    db.create_tables([UserStory], safe=True)


@app.before_request
def db_connect():
    db.connect()


@app.after_request
def db_close(respond):
    db.close()
    return respond


@app.route('/')
def homepage():
    return story_list()


@app.route('/list')
def story_list():
    userstories = UserStory.select()
    return render_template('list.html', userstories=userstories)


@app.route('/story/', methods=['GET', 'POST'])
def story_page():
    if request.method == 'POST':
        UserStory.create(story_title = request.form['story_title'], user_story=request.form['user_story'], criteria=request.form['criteria'],
                          b_value=request.form['b_value'], estimation=request.form['estimation'], status=request.form['status'])
        return redirect('/')
    else:
        return render_template('form.html', u_st='', submit='Create')


@app.route('/story/<story_id>', methods=['GET', 'POST'])
def update_story(story_id):
    if request.method == 'POST':
        UserStory.update(story_title = request.form['story_title'], user_story=request.form['user_story'], criteria=request.form['criteria'],
                         b_value=request.form['b_value'], estimation=request.form['estimation'],
                         status=request.form['status']).where(UserStory.id == story_id).execute()
        return redirect(url_for('homepage'))
    else:
        u_st = UserStory.get(UserStory.id == story_id)
        return render_template('form.html', u_st=u_st, submit='Update')


@app.route('/delete/<story_id>', methods=['GET'])
def delete_story(story_id):
    UserStory.delete().where(UserStory.id == story_id).execute()
    return redirect(url_for('homepage'))



if  __name__ == '__main__':
    create_tables()
    app.run()
