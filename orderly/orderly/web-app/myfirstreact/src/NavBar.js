import React, {Component} from 'react';

class NavBar extends Component {

    handleClick = (e) => {
        document.querySelector('.nav-selected').classList.remove('nav-selected');
        e.target.classList.add('nav-selected');
    }

    render() {
        return (
            <ul id="nav-bar">
                <li className="nav-selected" onClick={this.handleClick}>My households</li>
                <li onClick={this.handleClick}>My chores</li>
                <li onClick={this.handleClick}>Notifications</li>
            </ul>
        )
    }
}

export default NavBar;