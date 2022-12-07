import React from 'react';

function App() {

  const name = fetch('http://localhost:5000/customers/customer_info/gokul')

  return (
    <h1>Bill Manager</h1>
  );
}

export default App;
