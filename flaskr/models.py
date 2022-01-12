from flaskr import db

class Users(db.Model):
    """ Clase creada para trabajar el modelo ORM de los usuarios """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"<User => Username: {self.username}>"
