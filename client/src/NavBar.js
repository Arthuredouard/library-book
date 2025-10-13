import { Link } from 'react-router-dom';

function NavBar() {
  return (
    <nav>
      <Link to="/books">Books</Link> |{" "}
      <Link to="/authors">Authors</Link> |{" "}
      <Link to="/borrow">Borrow</Link>
    </nav>
  );
}

export default NavBar;

