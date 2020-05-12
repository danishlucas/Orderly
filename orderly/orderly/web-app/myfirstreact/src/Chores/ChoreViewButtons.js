import React, {Component} from 'react';

import { FaRegCalendar } from 'react-icons/fa';
import { FaBars } from 'react-icons/fa';

class ChoreViewButtons extends Component {
    constructor(props) {
        super(props);
        this.handleClick = this.handleClick.bind(this);
    }

    componentDidMount() {
        let selectedView = "#chore-view-" + this.props.initView;
        document.querySelector(selectedView).classList.add('chore-view-button-selected');
    }

    handleClick(e, view) {
        document.querySelector('.chore-view-button-selected').classList.remove('chore-view-button-selected');
        e.currentTarget.classList.add('chore-view-button-selected');
        this.props.setChoreView(view);
    };

    render() {
        return(
          <div id="chore-view">
              <button id="chore-view-list" className="chore-view-button" onClick={(e) => this.handleClick(e, 'list')}>
                  <FaBars id="list-icon" size={55}/></button>
              <button id="chore-view-calendar" className="chore-view-button" onClick={(e) => this.handleClick(e, 'calendar')}>
                  <FaRegCalendar id="calendar-icon" size={55}/></button>
          </div>
        );
    }
}

export default ChoreViewButtons