import React, {useState, useEffect} from "react";
import axios from 'axios';

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






//     const [examples, setWeather] = useState([]);

    
//     useEffect(() => {

//         axios.get('')
//       .then(response => {
//         setWeather(response.data.observations);
//       })
//       .catch(error => {
//         console.log(error);
//       });
//   }, []);


// // const rows = examples.map(example =>

// //     //key={example.id}
// //     <tr >
// //         <td>{example.wmo_id}</td>
// //         <td>{example.name}</td>
// //         <td>{example.website}</td>
// //         <td>{example.id}</td>
// //     </tr>);

// return (
//    
//     );
// }
