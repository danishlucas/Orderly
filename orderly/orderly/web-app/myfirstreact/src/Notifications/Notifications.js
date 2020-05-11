import React from 'react';
import ReactDOM from 'react-dom'
import './Notifications.css';

function Notifications(props) {
        return (
            <div id="notif">
                <div id="feed">This is where each task/event initiated by users will show up</div>
                <div id="options">This is the right column with some additional options</div>
            </div>
        )
}

const element = <Notifications/>;
ReactDOM.render(
    element,
    document.getElementById('root')
);

export default Notifications;
