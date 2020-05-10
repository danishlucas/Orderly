import React, {Component} from 'react';

import { FaChevronLeft } from 'react-icons/fa';
import { FaChevronRight } from 'react-icons/fa';

/*
    Allows the user to select between different days of the week, also shows week day of the week is currently selected.
 */
class DayOfWeekPicker extends Component {
    constructor(props) {
        super(props);
        this.state = {

        };
        this.sundayRef = React.createRef();
        this.mondayRef = React.createRef();
        this.tuesdayRef = React.createRef();
        this.wednesdayRef = React.createRef();
        this.thursdayRef = React.createRef();
        this.fridayRef = React.createRef();
        this.saturdayRef = React.createRef();
    }

    componentDidMount() {
        let dowArr = [this.sundayRef, this.mondayRef, this.tuesdayRef, this.wednesdayRef, this.thursdayRef,
            this.fridayRef, this.saturdayRef];
        dowArr[this.props.initDay].current.classList.add('dow-selected');
    }

    componentDidUpdate(prevProps, prevState, snapshot) {
        if (prevProps.initDay !== this.props.initDay) {
            let dowArr = [this.sundayRef, this.mondayRef, this.tuesdayRef, this.wednesdayRef, this.thursdayRef,
                this.fridayRef, this.saturdayRef];
            document.querySelector('.dow-selected').classList.remove('dow-selected');
            dowArr[this.props.initDay].current.classList.add('dow-selected');
        }
    }

    handleClick = (e, newDay, onClick) => {
        document.querySelector('.dow-selected').classList.remove('dow-selected');
        e.target.classList.add('dow-selected');
        onClick(newDay - this.props.initDay);
    };

    render() {
        return (
            <div>
                <ul id="dow-picker">
                    <li><button className="dow-button" onClick={() => this.props.onChevronClick(-1)}>
                        <FaChevronLeft className="dow-chevron" size={45}/></button></li>
                    <li><button className="dow-button" ref={this.sundayRef} onClick={(e) =>
                        this.handleClick(e, 0, this.props.onDayClick)}>S</button></li>
                    <li><button className="dow-button" ref={this.mondayRef} onClick={(e) =>
                        this.handleClick(e, 1, this.props.onDayClick)}>M</button></li>
                    <li><button className="dow-button" ref={this.tuesdayRef} onClick={(e) =>
                        this.handleClick(e, 2, this.props.onDayClick)}>T</button></li>
                    <li><button className="dow-button" ref={this.wednesdayRef} onClick={(e) =>
                        this.handleClick(e, 3, this.props.onDayClick)}>W</button></li>
                    <li><button className="dow-button" ref={this.thursdayRef} onClick={(e) =>
                        this.handleClick(e, 4, this.props.onDayClick)}>Th</button></li>
                    <li><button className="dow-button" ref={this.fridayRef} onClick={(e) =>
                        this.handleClick(e, 5, this.props.onDayClick)}>F</button></li>
                    <li><button className="dow-button" ref={this.saturdayRef} onClick={(e) =>
                        this.handleClick(e, 6, this.props.onDayClick)}>S</button></li>
                    <li><button className="dow-button" onClick={() => this.props.onChevronClick(1)}>
                        <FaChevronRight className="dow-chevron" size={45}/></button></li>
                </ul>
            </div>
        );
    }
}


export default DayOfWeekPicker