import React from 'react';
import './App.css';
import NavBar from "./NavBar";
import Households from "../Households/Households";

class App extends React.Component{
    constructor(props) {
        super(props);
        this.setPage = this.setPage.bind(this);
        this.state = {
            page: <Households/>
        }
    }

    render() {
        return (
            <div className="App">
                <h1 id="heading">Orderly</h1>
                <NavBar setPage={this.setPage}>Navigation bar</NavBar>
                {this.state.page}
            </div>
        );
    }

    setPage(currPage) {
        this.setState({
           page: currPage
        });
    }

}
export default App;
