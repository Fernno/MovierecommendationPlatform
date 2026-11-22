import "../styles/Hero.css";

function Hero() {
  return (
    <div className="hero">
      <div className="hero-content">
        <h1>Stranger Things</h1>

        <p>
          When a young boy vanishes, a town uncovers a mystery involving
          secret experiments and supernatural forces.
        </p>

        <div className="hero-buttons">
          <button>▶ Play</button>
          <button>ℹ More Info</button>
        </div>
      </div>
    </div>
  );
}

export default Hero;