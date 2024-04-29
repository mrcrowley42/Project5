import React, {useState, useEffect} from "react";



export default function Admin() {

  const [sources, setSources] = useState([])
    const [loading, setLoading] = useState(false)
    useEffect(() => {
      setLoading(true)
      fetch("http://127.0.0.1:8000/admin_api/")
        .then(response => response.json())
        .then(json => setSources(json))
        .finally(() => {
          setLoading(false)
        })
    }, [])


    

  return (
   <>
{loading ? 
            (<div>Loading...</div>) 
            : (

<>
              <h1>stuf</h1>
              <table border={1}>
                <tr>
                  <th>air_temp</th>
                  <th>dewpt</th>
                  <th>formatted datetime</th>
                </tr>
                {sources.map(obs => (

                    
                  <tr key={obs.id}>
                    <td>{obs.air_temp}</td>
                    <td>{obs.dewpt}</td>
                    <td>{obs.formatted_datetime}</td>
                    
                  </tr>
                ))}
              </table>
            </>

            )
}

      <button className="submitButton">Add Source +
      </button>
      <button className="submitButton" title="Click to ingest new data from sources" type="button">Do
        Manual Ingest
      </button>
      <button className="submitButton" title="Click to Reload the Webserver" type="button">Reload
        Server
      </button>
    </>
  )

  

}