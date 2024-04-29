import React, {useState, useEffect} from "react";

export default function WeatherTable(){
    const [observations, setObservations] = useState([])
    const [loading, setLoading] = useState(false)

    useEffect(() => {
      setLoading(true)
      fetch("http://127.0.0.1:8000/user?limit=10&wmo=8")
        .then(response => response.json())
        .then(json => setObservations(json[0].observations))
        .finally(() => {
          setLoading(false)
        })
    }, [setObservations])

    return (
        <>
        {loading ? 
            (<div>Loading...</div>) 
            :
            (<>
                <h1>stuf</h1>
                <table border={1}>
                    <thead>
                        <tr>
                        <th>air_temp</th>
                        <th>dewpt</th>
                        <th>formatted datetime</th>
                        </tr>
                    </thead>

                    {observations.map(obs => (
                    <tbody key={obs.id}>
                        <tr>
                        <td>{obs.air_temp}</td>
                        <td>{obs.dewpt}</td>
                        <td>{obs.formatted_datetime}</td>
                        </tr>
                    </tbody>
                    ))}
                    
                </table>
            </>)
        }
        </>
    );
}