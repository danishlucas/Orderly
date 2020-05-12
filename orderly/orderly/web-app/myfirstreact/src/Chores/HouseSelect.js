import React, {Component} from 'react';

import { FaHome } from 'react-icons/fa';

class HouseSelect extends Component {
    constructor(props) {
        super(props);
        this.handleClick = this.handleClick.bind(this);
    }

    componentDidUpdate(prevProps, prevState, snapshot) {
        if (this.props.choreView === 'list' && document.querySelector('.house-button-list-selected') == null) {
            document.querySelector('#house-init').classList.add('house-button-list-selected');
        }
    }

    handleClick(e) {
        if (this.props.choreView === 'list') {
            document.querySelector('.house-button-list-selected').classList.remove('house-button-list-selected');
            e.currentTarget.classList.add('house-button-list-selected');
        }
    }

    housePosition(index) {
        const style = {
            position: 'relative',
            width: '4em',
            left: (8 + 5 * index) + 'em'
        };

        return style;
    }

    render() {
        return(
          <div id='house-select'>
                <button id='house-init' className={'house-button-' + this.props.choreView} style={this.housePosition(0)}
                        onClick={this.handleClick}><FaHome size={45}/></button>
                <button className={'house-button-' + this.props.choreView} style={this.housePosition(1)}
                        onClick={this.handleClick}><FaHome size={45}/></button>
                <button className={'house-button-' + this.props.choreView} style={this.housePosition(2)}
                        onClick={this.handleClick}><FaHome size={45}/></button>
          </div>
        );
    }
}

export default HouseSelect