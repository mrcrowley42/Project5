import './style.css'
import ExampleList from './components/example-list';
import MyButton from './components/example-button';
import NavBar from './components/navigation-bar';
import WeatherTable from './components/weather-table';
import { BrowserRouter, Routes, Route, NavLink, Outlet } from 'react-router-dom';
import Dev from './pages/Dev';
import Admin from './pages/Admin';
import User from './pages/User';

function Index() {
  return (
    <>
      <h1>Home Page</h1>
      <p>
        Weather observations borrowed (stolen) from the BOM and displayed in new, life-changing ways.
      </p>
    </>
  )
}

function Other() {
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
            <Route path="/other" element={<Other />} />
          </Routes>
        </div>
      </div>
    </BrowserRouter>
  );
}
