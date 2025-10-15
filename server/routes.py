from flask import Blueprint, request, jsonify
from .models import Author, Book, User, BorrowedBook
from . import db

# Création du blueprint
bp = Blueprint('main', __name__)

# ------------------- ROUTE D’ACCUEIL -------------------
@bp.route('/')
def home():
    return "<h1>Library Project Server</h1>"

# ------------------- ROUTES BOOKS -------------------
@bp.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

@bp.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    if not data or 'title' not in data or 'author' not in data:
        return jsonify({'error': 'Missing data'}), 400
    book = Book(title=data['title'], author=data['author'])
    db.session.add(book)
    db.session.commit()
    return jsonify(book.to_dict()), 201

# ------------------- ROUTES AUTHORS -------------------
@bp.route('/authors', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    return jsonify([author.to_dict() for author in authors])

@bp.route('/authors', methods=['POST'])
def create_author():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Missing data'}), 400
    author
