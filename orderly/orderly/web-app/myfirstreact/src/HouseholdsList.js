import React, {Component} from 'react';

class HouseholdsList extends Component {

    handleClick = (e) => {
        document.querySelector('.house-selected').classList.remove('house-selected');
        e.target.classList.add('house-selected');
    }

    render() {
        return (
            <ul id="left-content">
                <li className="house-selected" onClick={this.handleClick}>UW dorm</li>
                <li onClick={this.handleClick}>Add household</li>
            </ul>
        )
    }
}

export default HouseholdsList;