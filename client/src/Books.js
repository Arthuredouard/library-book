import { useEffect, useState } from 'react';
import BookForm from './BookForm';

function Books() {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    fetch('/books')
      .then(res => res.json())
      .then(data => setBooks(data));
  }, []);

  return (
    <div>
      <h2>Books</h2>
      <BookForm />
      <ul>
        {books.map(book => (
          <li key={book.id}>{book.title} by {book.author}</li>
        ))}
      </ul>
    </div>
  );
}

export default Books;
