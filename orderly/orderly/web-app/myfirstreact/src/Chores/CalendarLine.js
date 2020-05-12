import React from 'react';

const lineStyle = {
    position: "relative",
    height: "1em",
    marginBottom: "1em"
};

function CalendarLine(props) {
    return (
        <div style={lineStyle}>
            <div className="calendar-time">{props.time}</div>
            <hr className="calendar-line"/>
        </div>
    );
}

export default CalendarLine