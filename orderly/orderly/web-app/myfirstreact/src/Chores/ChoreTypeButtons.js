import React, {Component} from 'react';

class ChoreTypeButtons extends Component {
    constructor(props) {
        super(props);
        this.handleClick = this.handleClick.bind(this);
    }

    componentDidMount() {
        let selectedType = '#' + this.props.initType + '-chores';
        document.querySelector(selectedType).classList.add('chore-type-btn-selected');
    }

    handleClick(e, type) {
        document.querySelector('.chore-type-btn-selected').classList.remove('chore-type-btn-selected');
        e.target.classList.add('chore-type-btn-selected');
        this.props.setChoreType(type);
    }

    render() {
        return(
          <div id="chore-type">
              <button id="upcoming-chores" className="chore-type-btn" onClick={(e) => this.handleClick(e, 'upcoming')}>
                  Upcoming Chores</button>
              <button id="completed-chores" className="chore-type-btn" onClick={(e) => this.handleClick(e, 'completed')}>
                  Completed Chores</button>
              <button id="overdue-chores" className="chore-type-btn" onClick={(e) => this.handleClick(e, 'overdue')}>
                  Overdue Chores</button>
          </div>
        );
    }
}

export default ChoreTypeButtons