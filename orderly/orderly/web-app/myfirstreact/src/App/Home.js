import React from 'react';
import './App.css';
import Households from "../Households/Households";
import NavBar from "./NavBar";

class Home extends React.Component{
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
                <NavBar setPage={this.setPage}/>
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
export default Home;
