import React, {Component} from 'react';

class HouseholdDetails extends Component {

    handleClick = (e) => {
        document.querySelector('.nav-selected').classList.remove('nav-selected');
        e.target.classList.add('nav-selected');
    }

    render() {
        return (
            <div id="right-content">
                <h2>UW dorm</h2>
                <ul id="house-details-list">
                    <li>Members</li>
                    <li>Schedule</li>
                    <li>Preferences</li>
                </ul>
            </div>
        )
    }
}

export default HouseholdDetails;