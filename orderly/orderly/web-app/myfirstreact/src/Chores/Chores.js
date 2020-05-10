import React, {Component} from 'react';

import './Chores.css';

import ChoreDate from "./ChoreDate";
import DateForm from "./DateForm";
import DayOfWeekPicker from "./DayOfWeekPicker";

class Chores extends Component {
    constructor(props) {
        super(props);
        let initDate = new Date();
        this.state = {
            dow: initDate.getDay(),
            day: initDate.getDate(),
            month: initDate.getMonth(),
            year: initDate.getFullYear(),
            monthNames: ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                "October", "November", "December"]
        };

        this.setDay = this.setDay.bind(this);
        this.setMonth = this.setMonth.bind(this);
        this.setYear = this.setYear.bind(this);
        this.moveDay = this.moveDay.bind(this);
        this.moveWeek = this.moveWeek.bind(this);
        this.moveDate = this.moveDate.bind(this);
    }

    setDay(day) {
        let newDate = new Date(this.state.year, this.state.month, this.state.day);
        newDate.setDate(day);
        this.setState(
            {
                dow: newDate.getDay(),
                day: newDate.getDate()
            }
        );
    }

    setMonth(month) {
        let newDate = new Date(this.state.year, this.state.month, this.state.day);
        newDate.setDate(1);
        newDate.setMonth(month);
        this.setState(
            {
                dow: newDate.getDay(),
                day: newDate.getDate(),
                month: newDate.getMonth()
            }
        );
    }

    setYear(year) {
        let newDate = new Date(this.state.year, this.state.month, this.state.day);
        newDate.setYear(year);
        this.setState(
            {
                dow: newDate.getDay(),
                year: newDate.getFullYear()
            }
        );
    }

    moveDay(numDays) {
        this.moveDate(numDays, 1);
    }

    moveWeek(numWeeks) {
        this.moveDate(numWeeks, 7);
    }

    moveDate(numMoves, step) {
        let newDate = new Date(this.state.year, this.state.month, this.state.day);
        newDate.setDate(newDate.getDate() + numMoves * step);
        this.setState(
            {
                dow: newDate.getDay(),
                day: newDate.getDate(),
                month: newDate.getMonth(),
                year: newDate.getFullYear()
            }
        );
    }

    render() {
        return (
            <div id="chores">
                <div id="left-column">
                    <ChoreDate day={this.state.day} month={this.state.monthNames[this.state.month]} year={this.state.year}/>
                    <DateForm label="Month" changeDate={(m) => this.setMonth(m-1)} start={this.state.month + 1} max="12" min="1"/>
                    <DateForm label="Year" changeDate={(y) => this.setYear(y)} start={this.state.year} max="10000" min="1"/>
                </div>

                <div id="middle-column">
                    <DayOfWeekPicker initDay={this.state.dow} onDayClick={this.moveDay} onChevronClick={this.moveWeek}/>
                </div>

                <div id="right-column">
                </div>
            </div>
        );
    }
}

export default Chores;