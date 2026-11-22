import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import MovieRow from "./components/MovieRow";
import "./styles/App.css";

import {
  trending,
  topRated,
  actionMovies,
  comedyMovies,
} from "./data/movies";

function App() {
  return (
    <div className="app">
      <Navbar />
      <Hero />

      <MovieRow title="Trending Now" movies={trending} />
      <MovieRow title="Top Rated" movies={topRated} />
      <MovieRow title="Action Movies" movies={actionMovies} />
      <MovieRow title="Comedy Movies" movies={comedyMovies} />
    </div>
  );
}

export default App;