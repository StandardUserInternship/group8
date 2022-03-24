from xmlrpc.client import DateTime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

#User login stuff
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    account_type = db.Column(db.Integer, index=True)
    date_created = db.Column(db.DateTime)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class DataSets(db.Model):
    file_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    file_name = db.Column(db.String(120))
    file_path = db.Column(db.String())

    def get_file_id(self):
        return self.file_id

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
