import React, {useState, useEffect} from "react";
import axios from 'axios';

export default function WeatherTable(){



    const [users, setUsers] = useState([])
    const [loading, setLoading] = useState(false)
    useEffect(() => {
      setLoading(true)
      fetch("http://127.0.0.1:8000/user?limit=10&wmo=2")
        .then(response => response.json())
        .then(json => setUsers(json))
        .finally(() => {
          setLoading(false)
        })
    }, [])

    return (
<>
        {loading ? (
            <div>Loading...</div>
          ) : (
            <>
              <h1>Users</h1>
              <table border={1}>
                <tr>
                  <th>Name</th>
                  <th>Email</th>
                  <th>Phone</th>
                </tr>
                {users.map(user => (

                    
                  <tr key={user.id}>
                    <td>{user.wmo_id}</td>
                    <td>{user.location}</td>
                    <td>{user.observations}</td>
                    
                  </tr>
                ))}
              </table>
            </>
          )}

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
