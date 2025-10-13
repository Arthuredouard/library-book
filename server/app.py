from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config

# Initialisation de l'app Flask
app = Flask(__name__)
app.config.from_object(Config)

# Extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

# Import des modèles
from models import Author, Book, User, BorrowedBook

# Route d'accueil
@app.route('/')
def home():
    return "<h1>Library Project Server</h1>"

# ------------------- ROUTES BOOKS -------------------

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    book = Book(title=data['title'], author=data['author'])
    db.session.add(book)
    db.session.commit()
    return jsonify(book.to_dict()), 201

# ------------------- ROUTES AUTHORS -------------------

@app.route('/authors', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    return jsonify([author.to_dict() for author in authors])

@app.route('/authors', methods=['POST'])
def create_author():
    data = request.get_json()
    author = Author(name=data['name'])
    db.session.add(author)
    db.session.commit()
    return jsonify(author.to_dict()), 201

# ------------------- ROUTES BORROWED BOOKS -------------------

@app.route('/borrowed_books', methods=['GET'])
def get_borrowed_books():
    borrowed = BorrowedBook.query.all()
    return jsonify([b.to_dict() for b in borrowed])

@app.route('/borrowed_books', methods=['POST'])
def borrow_book():
    data = request.get_json()
    borrow = BorrowedBook(
        user_id=data['user_id'],
        book_id=data['book_id'],
        borrow_date=data['borrow_date']
    )
    db.session.add(borrow)
    db.session.commit()
    return jsonify(borrow.to_dict()), 201

# ------------------- Lancement du serveur -------------------

if __name__ == '__main__':
    app.run(port=5555)
