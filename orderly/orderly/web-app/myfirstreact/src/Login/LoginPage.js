import React, {Component} from 'react';
import Home from "../App/Home";

class Households extends Component {

    handleClick = (e, page) => {
        this.props.setPage(page);
    };

    render() {
        return (
            <div id="content">
                <h2>Create an account</h2>
                <input type="text"/>
                <input type="text"/>
                <button onClick={(e) => this.handleClick(e, <Home/>)}>Create an account</button>
                <p>OR</p>
                <h2>Log in</h2>
                <input type="text"/>
                <input type="text"/>
                <button onClick={(e) => this.handleClick(e, <Home/>)}>Log in</button>
            </div>
        )
    }
}

export default Households;