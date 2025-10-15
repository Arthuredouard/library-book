from . import db
from datetime import datetime

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name}

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    author = db.relationship('Author', backref=db.backref('books', lazy=True))

    def to_dict(self):
        return {"id": self.id, "title": self.title, "author": self.author.name}

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name}

class BorrowedBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    borrow_date = db.Column(db.DateTime, default=datetime.utcnow)
    return_date = db.Column(db.DateTime, nullable=True)

    user = db.relationship('User', backref=db.backref('borrowed_books', lazy=True))
    book = db.relationship('Book', backref=db.backref('borrowed_books', lazy=True))

    def to_dict(self):
        return {
            "id": self.id,
            "user": self.user.name,
            "book": self.book.title,
            "borrow_date": self.borrow_date.isoformat(),
            "return_date": self.return_date.isoformat() if self.return_date else None
        }




