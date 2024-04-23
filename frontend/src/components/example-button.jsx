import { useState } from 'react';

export default function MyButton({multiplier}) {

    const [count, setCount] = useState(0);
    

    function handleClick() {
      setCount(count + 1);
    }
  
    return (
      <button onClick={handleClick} className="submitButton">
        Clicked {count * multiplier} times
      </button>
    );
  }