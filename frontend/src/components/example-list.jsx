const weather = [
{air_temp: 20, dew_point: 16, speed: 33, id: 1},
{air_temp: 23, dew_point: 26, speed: 63, id: 2},
{air_temp: 27, dew_point: 6, speed: 13, id: 3},
];

export default function ExampleList(){

const listitems = weather.map(weather =>
    <li key={weather.id}
    style={{color:weather.speed > 30 ? 'magenta' : 'darkblue'}}
    >
        {weather.air_temp}
    </li>

);

return (<ul>{listitems}</ul>);


}

