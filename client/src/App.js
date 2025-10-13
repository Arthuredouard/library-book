// client/src/App.js

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import NavBar from './NavBar';
import Books from './Books';
import Authors from './Authors';
import Borrow from './Borrow';
import './App.css'; 

function App() {
  return (
    <Router>
      <NavBar />
      <div className="container">
        <Routes>
          <Route path="/books" element={<Books />} />
          <Route path="/authors" element={<Authors />} />
          <Route path="/borrow" element={<Borrow />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;


