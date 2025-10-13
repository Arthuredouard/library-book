// client/src/Author.js
function Author({ author }) {
  if (!author || !author.name) {
    return <li className="author-item">Auteur inconnu</li>;
  }

  return (
    <li className="author-item">
      <strong>{author.name}</strong>
    </li>
  );
}

export default Author;

