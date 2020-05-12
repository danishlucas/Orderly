import React, {Component} from 'react';

class ChoreCalendarBox extends Component {
    render() {
        return (
            <div className="calendar-box" style={this.boxPosition()}>
                <div className="calendar-box-title">{this.props.choreTitle}</div>
            </div>
        );
    }

    boxPosition() {
        const style = {
            height: (2 * this.props.duration) + "em",
            width: "9em",
            left: (5.5 + 9 * this.props.index) + "em",
            top: (.7 + 2 * this.props.hour) + "em"
        };

        return style;
    }
}

export default ChoreCalendarBox