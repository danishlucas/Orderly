import React, {Component} from 'react';
import ChoreListBox from "./ChoreListBox";

class ChoreList extends Component {
    render() {
        return(
            <div id="chore-list">
                <ChoreListBox title='Vacuum' supplies='jjfhfhjf l;aksf;laksf as;dlkfj sd;lkfj asd;lkjsdf kjasdflkj as;lkasfd ;ljkasdf asd;sdflj ef' time={12}/>
                <ChoreListBox title='Vacuum' supplies='jjfhfhjf l;aksf;laksf as;dlkfj sd;lkfj asd;lkjsdf kjasdflkj as;lkasfd ;ljkasdf asd;sdflj ef' time={16}/>
            </div>
        )
    }
}

export default ChoreList