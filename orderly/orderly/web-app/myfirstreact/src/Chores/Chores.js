import React, {Component} from 'react';

import './Chores.css';

import ChoreDate from "./ChoreDate";
import DateForm from "./DateForm";
import DayOfWeekPicker from "./DayOfWeekPicker";
import ChoreTypeButtons from "./ChoreTypeButtons";
import ChoreViewButtons from "./ChoreViewButtons";
import HouseSelect from "./HouseSelect";
import ChoreCalendar from "./ChoreCalendar";
import ChoreList from "./ChoreList";

/*Used to specify what type view chores are displayed in*/
const ChoreView = {
    CALENDAR: 'calendar',
    LIST: 'list'
};

/*Used to specify what type of chore this page is displaying*/
const ChoreType = {
    UPCOMING: 'upcoming',
    COMPLETED: 'completed',
    OVERDUE: 'overdue'
};

/*
    Displays all of the chores for a user on a given day.
 */
class Chores extends Component {

    constructor(props) {
        super(props);
        let initDate = new Date();
        this.state = {
            choreView: ChoreView.CALENDAR,
            choreType: ChoreType.UPCOMING,
            viewPage: <ChoreCalendar/>,
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
        this.setChoreType = this.setChoreType.bind(this);
        this.setChoreView = this.setChoreView.bind(this);
    }

    /*Functions for setting the current date*/

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

    /*Functions for moving the date forward/backwards a set number of days/weeks/months etc..*/

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

    /*Functions for setting the type of chores to be displayed, and the view in which to display them*/

    setChoreType(type) {
        this.setState(
            {
                choreType: type
            }
        );
    }

    setChoreView(view) {
        let viewPage = <ChoreCalendar/>;
        if (view === ChoreView.LIST) {
            viewPage = <ChoreList/>
        }
        this.setState(
            {
                choreView: view,
                viewPage: viewPage
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
                    <ChoreTypeButtons initType={this.state.choreType} setChoreType={this.setChoreType}/>
                </div>

                <div id="middle-column">
                    <DayOfWeekPicker initDay={this.state.dow} onDayClick={this.moveDay} onChevronClick={this.moveWeek}/>
                    <HouseSelect choreView={this.state.choreView}/>
                    {this.state.viewPage}
                </div>

                <div id="right-column">
                    <ChoreViewButtons initView={this.state.choreView} setChoreView={this.setChoreView}/>
                </div>
            </div>
        );
    }
}

export default Chores;