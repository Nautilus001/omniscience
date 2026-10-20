import { useState, useEffect } from 'react'
import './App.css'
import type { Container } from './container'

function App() {
  const [containers, setContainers] = useState<Container[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    const query = "{ allContainers { name status } }";

    fetch('/api/graphql/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ query }),
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error('Network response was not ok');
        }
        return res.json();
      })
      .then((result) => {
        if (result.errors) {
          throw new Error(result.errors[0].message);
        }
        setContainers(result.data.allContainers || []);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  return (
    <>
      <section id="center">
        <div>
          <h1>Container Status</h1>
          <p>
            Verify that your containers are running properly, without SSHing 10,000 times.
          </p>
        </div>
      </section>

      <div className="ticks"></div>

      <section id="next-steps">
        <div id="docs">
          <h2>Monitored Containers</h2>
          
          {loading && <p>Loading container telemetry...</p>}
          {error && <p style={{ color: 'red' }}>Error: {error}</p>}

          {!loading && !error && containers.length === 0 && (
            <p>No containers found.</p>
          )}

          {!loading && !error && containers.length > 0 && (
            <ul className="container-list" style={{ listStyle: 'none', padding: 0 }}>
              {containers.map((container, index) => (
                <li key={index} style={{ margin: '10px 0', padding: '10px', background: '#1e1e1e', borderRadius: '6px', display: 'flex', justifyContent: 'space-between' }}>
                  <span style={{ fontWeight: 'bold' }}>{container.name}</span>
                  <span 
                    style={{ 
                      color: container.status === true ? '#4ade80' : '#f87171',
                      textTransform: 'uppercase'
                    }}
                  >
                    {container.status ? "good":"bad"}
                  </span>
                </li>
              ))}
            </ul>
          )}
        </div>
      </section>

      <div className="ticks"></div>
      <section id="spacer"></section>
    </>
  )
}

export default App