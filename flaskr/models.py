from flaskr import db
from werkzeug.security import check_password_hash, generate_password_hash

class Users(db.Model):
    """ Clase creada para trabajar el modelo ORM de los usuarios """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User => Id: {self.id}, Username: {self.username}>"
