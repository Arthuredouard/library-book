from app import app, db
from models import Author, Book, User, BorrowedBook

with app.app_context():
    print("Seeding database with Haitian authors...")

    # Vider les tables
    BorrowedBook.query.delete()
    Book.query.delete()
    Author.query.delete()
    User.query.delete()

    # Auteurs haïtiens
    a1 = Author(name="Frankétienne")
    a2 = Author(name="Dany Laferrière")
    a3 = Author(name="Yanick Lahens")
    a4 = Author(name="Gary Victor")
    a5 = Author(name="René Depestre")

    db.session.add_all([a1, a2, a3, a4, a5])

    # Livres associés
    b1 = Book(title="Dézafi", author="Frankétienne")
    b2 = Book(title="L'énigme du retour", author="Dany Laferrière")
    b3 = Book(title="Dans la maison du père", author="Yanick Lahens")
    b4 = Book(title="Le sang et la mer", author="Gary Victor")
    b5 = Book(title="Hadriana dans tous mes rêves", author="René Depestre")

    db.session.add_all([b1, b2, b3, b4, b5])

    # Utilisateurs
    u1 = User(name="Marie")
    u2 = User(name="Jean")
    db.session.add_all([u1, u2])

    # Emprunts
    borrow1 = BorrowedBook(user_id=1, book_id=1, borrow_date="2025-10-12")
    borrow2 = BorrowedBook(user_id=2, book_id=3, borrow_date="2025-10-13")
    db.session.add_all([borrow1, borrow2])

    db.session.commit()
    print("Seeding complete.")
