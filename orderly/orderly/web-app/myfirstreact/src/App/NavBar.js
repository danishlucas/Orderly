import React, {Component} from 'react';

import Households from "../Households/Households";
import Notifications from "../Notifications/Notifications";
import Chores from "../Chores/Chores";

class NavBar extends Component {

    handleClick = (e, page) => {
        document.querySelector('.nav-selected').classList.remove('nav-selected');
        e.target.classList.add('nav-selected');
        this.props.setPage(page);
    };

    render() {
        return (
            <ul id="nav-bar">
                <li className="nav-selected" onClick={(e) => this.handleClick(e, <Households/>)}>Households</li>
                <li onClick={(e) => this.handleClick(e, <Chores/>)}>Chores</li>
                <li onClick={(e) => this.handleClick(e, <Notifications/>)}>Notifications</li>
            </ul>
        )
    }
}

export default NavBar;