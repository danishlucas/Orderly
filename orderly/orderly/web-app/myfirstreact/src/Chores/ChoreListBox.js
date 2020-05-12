import React, {Component} from 'react';

class ChoreListBox extends Component {
    constructor(props) {
        super(props);
        this.state = {
            descDisplay: "none"
        };
        this.handleClick = this.handleClick.bind(this);
    }

    handleClick(e) {
        e.target.classList.toggle('clb-desc-button-selected');
        let newDisplay = 'none';
        if (this.state.descDisplay === 'none') {
            newDisplay = 'block';
        }
        this.setState(
            {
                descDisplay: newDisplay
            }
        )
    }

    render() {
        const times = ["12:00 AM", " 1:00 AM", " 2:00 AM", " 3:00 AM", " 4:00 AM", " 5:00 AM", " 6:00 AM",
            " 7:00 AM", " 8:00 AM", " 9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", " 1:00 PM",
            " 2:00 PM", " 3:00 PM", " 4:00 PM", " 5:00 PM", " 6:00 PM", " 7:00 PM", " 8:00 PM",
            " 9:00 PM", "10:00 PM", "11:00 PM", "12:00 AM"];

        return(
            <div>
                <div className="chore-list-box">
                    <div className="chore-list-box-left">
                        <div className="clb-title">{this.props.title}</div>
                        <div className="clb-supplies-title">Supplies:</div>
                        <div className="clb-supplies">{this.props.supplies}</div>
                    </div>
                    <div className="chore-list-box-right">
                        <div className="clb-time">{times[this.props.time]}</div>
                        <button className="clb-desc-button" onClick={this.handleClick}>description</button>
                    </div>
                </div>
                <div className="chore-list-desc-box" style={{display: this.state.descDisplay}}>
                    <div className="chore-list-desc">
                        lksjdfkjsdjs ljsdf ;ksdf ;ljsdf ;ljsdf ;lkjsdf ;lkjsdf ;lkjsdf laf l;jasdf ;lkjasdf lsajdf
                        ljasdf ;ljsdf ljsdf l;kjasdf ;lksjdfl;akjsdf;sd ;kajsdf ;lksjd ;lasdf ;lsjdf a;sdjf ;alksjdf
                        ;lasjkdf lkjasdf ;lsjdf laskjdf ;lsjkadf l;jsdf ;ljsdf ;lkjsdf ;lksjdf ;lksjdf
                    </div>
                </div>
            </div>
        )
    }
}

export default ChoreListBox