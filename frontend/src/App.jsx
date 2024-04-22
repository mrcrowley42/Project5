import './style.css'
import ExampleList from './components/example-list';
import MyButton from './components/example-button';
import NavBar from './components/navigation-bar';

export default function App() {
  return (
    <div className="App">
      <NavBar />
      <div className='content'>
      <ExampleList />
    <MyButton />
    </div>
    </div>  
  );
}

