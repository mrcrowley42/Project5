import './style.css'
import ExampleList from './components/example-list';
import MyButton from './components/example-button';
import NavBar from './components/navigation-bar';
import WeatherTable from './components/weather-table';
import { BrowserRouter, Routes, Route, NavLink, Outlet } from 'react-router-dom';

function Index() {
  return (
    <>
      <ExampleList />
    <MyButton multiplier={3} />
    <MyButton multiplier={13} />
    <WeatherTable />


      <MyButton />
    </>
  )
}

function Other() {
  return (
    <div>Othererer!</div>
  )
}

function Dev() {
  return (
    <div>dev page!</div>
  )
}


function Admin() {
  return (
    <div>admin page!</div>
  )
}

function User() {
  return (
    <div>user page!</div>
  )
}

export default function App() {
  return (
      <BrowserRouter>
        <div className='App'>
          <NavBar />
          <div className='content'>

          <Routes>
            <Route path="/" element={<Index />} />
            <Route path="/dev" element={<Dev />} />
            <Route path="/admin" element={<Admin />} />
            <Route path="/user" element={<User />} />
          </Routes>
      </div>
      </div>
      </BrowserRouter>
  );
}
