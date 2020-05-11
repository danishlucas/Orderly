import React, {Component} from 'react';
import { Link } from "@reach/router"
import { FormGroup, InputGroup } from "@blueprintjs/core";

class Households extends Component {

    nextPath(path) {
        this.props.history.push(path);
    }

    render() {
        return (
            <>
                <FormGroup
                    label="Email"
                    labelFor="text-input"
                    inline={true}
                >
                    <InputGroup id="email" placeholder="E-mail address" />
                </FormGroup>
                <FormGroup
                    label="Password"
                    labelFor="text-input"
                    inline={true}
                >
                    <InputGroup id="password" placeholder="Password" />
                </FormGroup>
                <Link to="home">
                    <button>Create an account</button>
                </Link>
                <p>OR</p>
                <h2>Log in</h2>
                <FormGroup
                    label="Email"
                    labelFor="text-input"
                    inline={true}
                >
                    <InputGroup id="email" placeholder="E-mail address" />
                </FormGroup>
                <FormGroup
                    label="Password"
                    labelFor="text-input"
                    inline={true}
                >
                    <InputGroup id="password" placeholder="Password" />
                </FormGroup>
                <Link to="home">
                    <button>Login</button>
                </Link>
            </>
        )
    }
}

export default Households;