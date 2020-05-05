import React, {Component} from 'react';

class NavBar extends Component {

    handleClick = (e) => {
        document.querySelector('.selected').classList.remove('selected');
        e.target.classList.add('selected');
    }

    render() {
        return (
            <ul id="nav_bar">
                <li className="selected" onClick={this.handleClick}>My households</li>
                <li onClick={this.handleClick}>My chores</li>
                <li onClick={this.handleClick}>Notifications</li>
            </ul>
        )
    }
}

export default NavBar;