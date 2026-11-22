import "../styles/Navbar.css";

function Navbar() {
  return (
    <nav className="navbar">
      <h1 className="logo">NETFLIX</h1>

      <ul className="nav-links">
        <li>Home</li>
        <li>Movies</li>
        <li>Series</li>
        <li>My List</li>
      </ul>

      <div className="profile">👤</div>
    </nav>
  );
}

export default Navbar;