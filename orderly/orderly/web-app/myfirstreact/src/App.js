import React from 'react';
import './App.css';
import NavBar from "./NavBar";
import HouseholdsList from "./HouseholdsList";
import HouseholdDetails from "./HouseholdDetails";

function App() {
  return (
    <div className="App">
        <h1 id="heading">Orderly</h1>
        <NavBar>Navigation bar</NavBar>
        <div id="content">
            <HouseholdsList></HouseholdsList>
            <HouseholdDetails></HouseholdDetails>
        </div>
    </div>
  );
}

export default App;
