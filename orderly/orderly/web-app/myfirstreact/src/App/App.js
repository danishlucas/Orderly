import React from 'react';
import './App.css';
import Login from '../Login/Login';
import { Router } from "@reach/router"
import Home from './Home';


class App extends React.Component{

    render() {
        return (
            <div className="App">
                <h1 id="heading">Orderly</h1>

                <Router>
                    <Login path="/"/>
                    <Home path="home"/>
                </Router>
            </div>
        );
    }

}
export default App;
