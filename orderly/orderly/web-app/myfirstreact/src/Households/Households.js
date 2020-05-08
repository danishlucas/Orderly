import React, {Component} from 'react';
import HouseholdsList from "./HouseholdsList";
import HouseholdsDetails from "./HouseholdsDetails";

class Households extends Component {

    render() {
        return (
            <div id="content">
                <HouseholdsList/>
                <HouseholdsDetails/>
            </div>
        )
    }
}

export default Households;