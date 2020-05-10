import React, {Component} from 'react';

class ChoreDate extends Component {
    render() {
        return (
            <div id="chore-date">
                {this.props.month} {this.props.day}, {this.props.year}
            </div>
        )
    }
}

export default ChoreDate;