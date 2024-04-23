import React, {useState, useEffect} from "react";


export default function WeatherTable(){

    const [examples, setWeather] = useState([]);

    
    useEffect(() => {

        // fetch("https://jsonplaceholder.typicode.com/users")
        fetch("http://127.0.0.1:8000/user?limit=10&wmo=2")
        .then(response => response.json())
        .then(data => setWeather(data))
        .catch(err => console.log(err))},[])

const rows = examples.map(example =>

    //key={example.id}
    <tr >
        <td>{example.wmo_id}</td>
        <td>{example.location}</td>
        <td>{example.website}</td>
        <td>{example.id}</td>
    </tr>);

return (
<table>
    <thead>
    <tr>
        <th>Name</th>
        <th>E-mail</th>
        <th>Site</th>
        <th>ID</th>
    </tr>
    </thead>
    <tbody>
{rows}
    </tbody>
    

</table>

    );
}