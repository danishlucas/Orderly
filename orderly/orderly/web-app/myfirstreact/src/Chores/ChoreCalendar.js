import React, {Component} from 'react';
import CalendarLine from "./CalendarLine";
import ChoreCalendarBox from "./ChoreCalendarBox";

class ChoreCalendar extends Component {
    render() {
        const times = ["12:00 AM", " 1:00 AM", " 2:00 AM", " 3:00 AM", " 4:00 AM", " 5:00 AM", " 6:00 AM",
                       " 7:00 AM", " 8:00 AM", " 9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", " 1:00 PM",
                       " 2:00 PM", " 3:00 PM", " 4:00 PM", " 5:00 PM", " 6:00 PM", " 7:00 PM", " 8:00 PM",
                       " 9:00 PM", "10:00 PM", "11:00 PM", "12:00 AM"];

        return (
            <div id="chore-calendar">
                <ChoreCalendarBox choreTitle="Vacuum" index={0} hour={7} duration={6}/>
                <ChoreCalendarBox choreTitle="Vacuum" index={1} hour={5} duration={6}/>
                <ChoreCalendarBox choreTitle="Vacuum" index={2} hour={3} duration={6}/>
                {times.map((value) => {
                    return <CalendarLine time={value}/>})}
            </div>
        );
    }
}

export default ChoreCalendar