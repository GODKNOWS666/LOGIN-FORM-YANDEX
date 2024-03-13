import sqlalchemy
import sqlalchemy.ext.declarative as dec
from flask import Flask

from class_user import User

import db_session

SqlAlchemyBase = dec.declarative_base()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class Jobs(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("users.id"))
    job = sqlalchemy.Column(sqlalchemy.String)
    work_size = sqlalchemy.Column(sqlalchemy.Integer)
    collaborators = sqlalchemy.Column(sqlalchemy.String)
    start_date = sqlalchemy.Column(sqlalchemy.Date)
    end_date = sqlalchemy.Column(sqlalchemy.Date)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean)


def main():
    db_session.global_init("db/mars_explorer.db")
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"

    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    app.run()
