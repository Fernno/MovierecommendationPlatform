import "../styles/MovieRow.css";

function MovieRow({ title, movies }) {
  return (
    <div className="row">
      <h2>{title}</h2>

      <div className="row-posters">
        {movies.map((movie, index) => (
          <div key={index} className="movie-card">
            <img src={movie.image} alt={movie.title} />

            <div className="overlay">
              <h4>{movie.title}</h4>
              <button>▶</button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default MovieRow;