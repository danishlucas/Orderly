import React from 'react';
import './App.css';
import LoginPage from '../Login/LoginPage';
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
} from "react-router-dom";
import Home from './Home';

class App extends React.Component{
    constructor(props) {
        super(props);
        this.setPage = this.setPage.bind(this);
        this.state = {
            page: <LoginPage setPage={this.setPage}/>
        }
    }

    render() {
        return (
            <Router>
                <div className="App">
                    <h1 id="heading">Orderly</h1>
                    {this.state.page}

                    <Switch>
                        <Route path="/home">
                            <Home />
                        </Route>
                        <Route path="/">
                            <LoginPage />
                        </Route>
                    </Switch>
                </div>
            </Router>
        );
    }

    setPage(currPage) {
        this.setState({
           page: currPage
        });
    }

}
export default App;
