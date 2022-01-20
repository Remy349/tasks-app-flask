from flaskr import db
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash

class Users(db.Model):
    """ Clase creada para trabajar el modelo ORM de los usuarios """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    tasks = db.relationship("Tasks", backref="author", lazy="dynamic")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User => Id: {self.id}, Username: {self.username}>"

class Tasks(db.Model):
    """ Clase para crear el modelo de las tareas """
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String(160), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __repr__(self):
        return f"<Tasks => Id: {self.id}, Title: {self.title}, Description: {self.description}\
                Timestamp: {self.timestamp}, UserId: {self.user_id}>"
