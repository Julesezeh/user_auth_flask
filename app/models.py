from app.extensions import db


class User(db.Model):
    __tablename__ = "user"
    username = db.Column(db.String(), primary_key=True)
    password = db.Column(db.LargeBinary())

    def __repr__(self):
        return "User: " + self.username

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
