import React, {Component} from 'react';

class DateForm extends Component {
    constructor(props) {
        super(props);
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event) {
        this.setState({date: event.target.value});
        this.props.changeDate(event.target.value)
    }

    render() {
        return (
            <form>
                <label>{this.props.label}:</label><br/>
                <input id="date-spinner" type="number" max={this.props.max} min={this.props.min}
                       value={this.props.start} onChange={this.handleChange}/>
            </form>
        );
    }
}

export default DateForm;