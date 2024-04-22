import './style.css'
import ExampleList from './components/example-list';
import MyButton from './components/example-button';
import NavBar from './components/navigation-bar';
import { BrowserRouter, Routes, Route, NavLink, Outlet } from 'react-router-dom';

function Index() {
  return (
    <div className='content'>
      <ExampleList />
      <MyButton />
    </div>
  )
}

function Other() {
  return (
    <div>Othererer!</div>
  )
}

export default function App() {
  return (
      <BrowserRouter>
        <div className='App'>
          <NavBar />

          <Routes>
            <Route path="/" element={<Index />} />
            <Route path="/other" element={<Other />} />
          </Routes>
      </div>
      </BrowserRouter>
  );
}
